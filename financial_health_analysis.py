import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import PartialDependenceDisplay
from scipy.stats import kruskal, skew
import os, sys

sys.stdout.reconfigure(encoding='utf-8')

# Bảng màu
COLORS = {
    'primary': '#FF8C00',
    'accent1': '#FFA500',
    'accent2': '#FF7F50',
    'negative': '#DC143C',
    'neutral': '#8B95A5'
}
sns.set_theme(style='whitegrid', rc={"axes.spines.top": False, "axes.spines.right": False})
sns.set_palette([COLORS['primary'], COLORS['accent1'], COLORS['accent2']])

CHART_DIR = os.path.join(os.path.dirname(__file__), "output", "charts")
os.makedirs(CHART_DIR, exist_ok=True)

DATA_DIR = os.path.join(os.path.dirname(__file__), "ĐỀ BÀI", "DATASET")
df = pd.read_csv(os.path.join(DATA_DIR, "consumer_financial_health_engagement_2025.csv"))

print("=" * 70)
print("PHASE 3: FINANCIAL HEALTH ANALYSIS (BI REPORT)")
print("=" * 70)
print(f"Loaded {df.shape[0]:,} records. Charts will be saved to /output/charts/\n")

# ---- 3.1 Phân bố Health Score + Xu hướng theo tháng ----
print("[3.1] FINANCIAL HEALTH SCORE: DISTRIBUTION & TRENDS")
print(f"  - Mean: {df['financial_health_score'].mean():.2f} | Median: {df['financial_health_score'].median():.2f}")
print(f"  - Min: {df['financial_health_score'].min():.2f} | Max: {df['financial_health_score'].max():.2f}")
print(f"  - 25th percentile: {df['financial_health_score'].quantile(0.25):.2f}")
print(f"  - Records below 40 (Risk): {(df['financial_health_score'] < 40).sum()} ({(df['financial_health_score'] < 40).mean()*100:.1f}%)")
print(f"  - Records below 50 (Warning): {(df['financial_health_score'] < 50).sum()} ({(df['financial_health_score'] < 50).mean()*100:.1f}%)")
print(f"  - Std: {df['financial_health_score'].std():.2f}")
print(f"  - Skewness: {skew(df['financial_health_score'].dropna()):.4f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

sns.histplot(data=df, x='financial_health_score', bins=30, kde=True, color=COLORS['primary'], ax=ax1)
ax1.set_title('Financial Health Score Distribution', fontweight='bold', pad=15)
ax1.set_xlabel('Financial Health Score')
ax1.set_ylabel('Number of Consumer-Months')
ax1.axvline(x=40, color=COLORS['negative'], linestyle='--', linewidth=2, label='Risk Threshold (<40)')
ax1.axvline(x=50, color=COLORS['accent2'], linestyle='--', linewidth=1.5, label='Warning Zone (<50)')
ax1.legend()

# Xu hướng theo tháng
df['analysis_month_dt'] = pd.to_datetime(df['analysis_month'])
df['month_num'] = df['analysis_month_dt'].dt.month
trend = df.groupby('month_num')['financial_health_score'].mean().reset_index()
sns.lineplot(data=trend, x='month_num', y='financial_health_score', marker='o',
             color=COLORS['primary'], linewidth=2.5, markersize=8, ax=ax2)
ax2.set_title('Average Health Score Over 12 Months (2025)', fontweight='bold', pad=15)
ax2.set_xlabel('Month')
ax2.set_ylabel('Average Score')
ax2.set_xticks(range(1, 13))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.suptitle('3.1 Financial Health: Distribution and Temporal Trends', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout(pad=2.0)
plt.savefig(os.path.join(CHART_DIR, "3_1_health_distribution_trends.png"), dpi=300, bbox_inches='tight')
plt.show()

# Phân bổ theo segment
print("\n  Breakdown by Financial Health Segment:")
seg_stats = df.groupby('financial_health_segment')['financial_health_score'].agg(['count', 'mean', 'median'])
seg_stats['pct'] = seg_stats['count'] / seg_stats['count'].sum() * 100
seg_stats = seg_stats.sort_values('mean', ascending=False)
for seg, row in seg_stats.iterrows():
    print(f"    {seg}: n={int(row['count']):,}, {row['pct']:.1f}%, mean={row['mean']:.1f}, median={row['median']:.1f}")

seg_order = seg_stats.index.tolist()
seg_colors = [COLORS['accent1'] if m >= 60 else COLORS['accent2'] if m >= 50 else COLORS['negative']
              for m in seg_stats['mean']]
fig_seg, (ax_s1, ax_s2) = plt.subplots(1, 2, figsize=(16, 6))

ax_s1.barh(seg_order, seg_stats['count'], color=seg_colors)
ax_s1.set_title('Number of Records by Segment', fontweight='bold', pad=15)
ax_s1.set_xlabel('Number of Consumer-Month Records')
for i, (cnt, pct) in enumerate(zip(seg_stats['count'], seg_stats['pct'])):
    ax_s1.text(cnt + 30, i, f'{int(cnt):,} ({pct:.1f}%)', va='center', fontsize=10)
ax_s1.invert_yaxis()

sns.boxplot(data=df, y='financial_health_segment', x='financial_health_score',
            order=seg_order, palette=seg_colors, ax=ax_s2)
ax_s2.set_title('Score Distribution by Segment', fontweight='bold', pad=15)
ax_s2.set_xlabel('Financial Health Score')
ax_s2.set_ylabel('')

plt.suptitle('3.1b Financial Health Breakdown by Segment', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout(pad=2.0)
plt.savefig(os.path.join(CHART_DIR, "3_1b_segment_breakdown.png"), dpi=300, bbox_inches='tight')
plt.show()

# ---- 3.2 Drivers (Correlation + Random Forest) ----
print("\n[3.2] DRIVERS OF LOW FINANCIAL HEALTH")
features = ['spend_to_income_ratio', 'credit_utilization_ratio', 'essential_spend_ratio',
            'online_spend_ratio', 'spending_volatility', 'engagement_score']

corr = df[features + ['financial_health_score']].corr()['financial_health_score'].drop('financial_health_score').sort_values()
print("  Pearson Correlation with financial_health_score:")
for feat, val in corr.items():
    print(f"    {feat:30s}: {val:+.4f}")

X = df[features].fillna(0)
y = df['financial_health_score']
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X, y)
fi = pd.DataFrame({'Feature': features, 'Importance': rf.feature_importances_}).sort_values('Importance', ascending=False)
print("\n  Random Forest Feature Importance:")
for _, row in fi.iterrows():
    print(f"    {row['Feature']:30s}: {row['Importance']*100:.1f}%")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

sns.barplot(x=corr.values, y=corr.index, ax=ax1,
            palette=[COLORS['negative'] if x < 0 else COLORS['accent1'] for x in corr.values])
ax1.set_title('Pearson Correlation with Health Score', fontweight='bold', pad=15)
ax1.set_xlabel('Correlation Coefficient (r)')
ax1.set_ylabel('')

sns.barplot(data=fi, x='Importance', y='Feature', color=COLORS['primary'], ax=ax2)
ax2.set_title('Feature Importance (Random Forest)', fontweight='bold', pad=15)
ax2.set_xlabel('Importance Score')
ax2.set_ylabel('')

plt.suptitle('3.2 Key Drivers Impacting Financial Health', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout(pad=2.0)
plt.savefig(os.path.join(CHART_DIR, "3_2_drivers_correlation_fi.png"), dpi=300, bbox_inches='tight')
plt.show()

# Partial Dependence Plots cho top 3
print("\n  Partial Dependence Plots for top 3 drivers:")
top3_features = fi['Feature'].head(3).tolist()
top3_indices = [features.index(f) for f in top3_features]
print(f"    Features: {top3_features}")

fig_pdp, axes_pdp = plt.subplots(1, 3, figsize=(18, 5))
for i, (feat_idx, feat_name) in enumerate(zip(top3_indices, top3_features)):
    PartialDependenceDisplay.from_estimator(
        rf, X, [feat_idx], ax=axes_pdp[i],
        line_kw={'color': COLORS['primary'], 'linewidth': 2.5}
    )
    axes_pdp[i].set_title(f'PDP: {feat_name}', fontweight='bold', fontsize=11)
    axes_pdp[i].set_ylabel('Partial Dependence' if i == 0 else '')

plt.suptitle('3.2b Partial Dependence Plots — Top 3 Drivers', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout(pad=2.0)
plt.savefig(os.path.join(CHART_DIR, "3_2b_partial_dependence.png"), dpi=300, bbox_inches='tight')
plt.show()

# ---- 3.3 Khác biệt theo nhân khẩu học ----
print("\n[3.3] DEMOGRAPHIC DIFFERENCES")

# Chia nhóm tuổi (min age = 15)
df['age_group'] = pd.cut(df['age'], bins=[15, 25, 35, 45, 60, 100], labels=['15-25', '26-35', '36-45', '46-60', '60+'])

# Lấy top 10 nghề (dataset có 396 nghề, vẽ hết sẽ vỡ chart)
top_occ = df['occupation'].value_counts().head(10).index
df_top_occ = df[df['occupation'].isin(top_occ)]

top_prov = df['province_city'].value_counts().head(5).index
df_top_prov = df[df['province_city'].isin(top_prov)]

print("  Age Group Stats:")
age_stats = df.groupby('age_group', observed=False)['financial_health_score'].agg(['mean', 'median'])
for grp, row in age_stats.iterrows():
    print(f"    {grp}: mean={row['mean']:.1f}, median={row['median']:.1f}")

print("\n  Top 10 Occupation Stats (sorted by mean):")
occ_stats = df_top_occ.groupby('occupation')['financial_health_score'].agg(['mean', 'median']).sort_values('mean')
for occ, row in occ_stats.iterrows():
    print(f"    {occ:40s}: mean={row['mean']:.1f}, median={row['median']:.1f}")

print("\n  Top 5 Province Stats (sorted by mean):")
prov_stats = df_top_prov.groupby('province_city')['financial_health_score'].agg(['mean', 'median']).sort_values('mean')
for prov, row in prov_stats.iterrows():
    print(f"    {prov:30s}: mean={row['mean']:.1f}, median={row['median']:.1f}")

fig, axes = plt.subplots(1, 3, figsize=(20, 7))

sns.violinplot(data=df, x='age_group', y='financial_health_score', color=COLORS['accent1'], ax=axes[0],
               order=['15-25', '26-35', '36-45', '46-60', '60+'], inner='box', linewidth=1.2)
axes[0].set_title('By Age Group', fontweight='bold', pad=15)
axes[0].set_xlabel('Age Group')
axes[0].set_ylabel('Financial Health Score')

sns.violinplot(data=df_top_occ, y='occupation', x='financial_health_score', color=COLORS['accent2'], ax=axes[1],
               order=occ_stats.index, inner='box', linewidth=1.2)
axes[1].set_title('By Top 10 Occupations', fontweight='bold', pad=15)
axes[1].set_xlabel('Financial Health Score')
axes[1].set_ylabel('')

sns.violinplot(data=df_top_prov, y='province_city', x='financial_health_score', color=COLORS['primary'], ax=axes[2],
               order=prov_stats.index, inner='box', linewidth=1.2)
axes[2].set_title('By Top 5 Provinces', fontweight='bold', pad=15)
axes[2].set_xlabel('Financial Health Score')
axes[2].set_ylabel('')

plt.suptitle('3.3 Demographic Differences in Financial Health', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout(pad=2.0)
plt.savefig(os.path.join(CHART_DIR, "3_3_demographic_differences.png"), dpi=300, bbox_inches='tight')
plt.show()

# Kruskal-Wallis test
print("\n  Statistical Significance Tests (Kruskal-Wallis):")

age_groups_data = [grp['financial_health_score'].values for _, grp in df.groupby('age_group', observed=False)]
kw_age_stat, kw_age_p = kruskal(*age_groups_data)
print(f"    Age groups:      H={kw_age_stat:.2f}, p={kw_age_p:.4e} {'(Significant)' if kw_age_p < 0.05 else '(Not significant)'}")

occ_groups_data = [grp['financial_health_score'].values for _, grp in df_top_occ.groupby('occupation')]
kw_occ_stat, kw_occ_p = kruskal(*occ_groups_data)
print(f"    Occupations:     H={kw_occ_stat:.2f}, p={kw_occ_p:.4e} {'(Significant)' if kw_occ_p < 0.05 else '(Not significant)'}")

prov_groups_data = [grp['financial_health_score'].values for _, grp in df_top_prov.groupby('province_city')]
kw_prov_stat, kw_prov_p = kruskal(*prov_groups_data)
print(f"    Provinces:       H={kw_prov_stat:.2f}, p={kw_prov_p:.4e} {'(Significant)' if kw_prov_p < 0.05 else '(Not significant)'}")

# ---- 3.4 Crossover: Stressed x Engaged ----
print("\n[3.4] CROSSOVER SEGMENT: STRESSED x ENGAGED")
print(f"  Cutoff justification:")
print(f"    - Health < 50: Captures both 'Critical' (<40, dataset flag) and 'Warning Zone' (40-50)")
print(f"      Bottom 4.8% of all records ({(df['financial_health_score'] < 50).sum()} records)")
eng_median = df['engagement_score'].median()
print(f"    - Engagement > {eng_median:.1f} (dataset median): Data-driven cutoff using the median")
print(f"      to ensure balanced, meaningful comparison between Engaged vs. Disengaged groups")

# Tạo 4 nhóm quadrant
stressed_engaged = df[(df['financial_health_score'] < 50) & (df['engagement_score'] > eng_median)]
nonstressed_engaged = df[(df['financial_health_score'] >= 50) & (df['engagement_score'] > eng_median)]
stressed_disengaged = df[(df['financial_health_score'] < 50) & (df['engagement_score'] <= eng_median)]
nonstressed_disengaged = df[(df['financial_health_score'] >= 50) & (df['engagement_score'] <= eng_median)]

unique_consumers = stressed_engaged['consumer_id'].nunique()
print(f"\n  Segment size: {len(stressed_engaged)} consumer-month records")
print(f"  Unique consumers: {unique_consumers}")
print(f"  Recommended action: Non-punitive digital interventions (budgeting tools, spend alerts)")

# Profile chi tiết nhóm Stressed & Engaged
print(f"\n  Profile of Stressed & Engaged segment ({unique_consumers} unique consumers):")
for col in ['financial_health_score', 'engagement_score', 'spend_to_income_ratio',
            'credit_utilization_ratio', 'essential_spend_ratio', 'online_spend_ratio', 'spending_volatility']:
    print(f"    Avg {col:30s}: {stressed_engaged[col].mean():.3f}")

se_consumers = stressed_engaged.drop_duplicates('consumer_id')

print(f"\n  Top 5 Occupations (of {unique_consumers} unique consumers):")
for occ, cnt in se_consumers['occupation'].value_counts().head(5).items():
    print(f"    {occ}: {cnt} consumers ({cnt/unique_consumers*100:.1f}%)")

print(f"\n  Top 5 Provinces:")
for prov, cnt in se_consumers['province_city'].value_counts().head(5).items():
    print(f"    {prov}: {cnt} consumers ({cnt/unique_consumers*100:.1f}%)")

# Tuổi
se_consumers = se_consumers.copy()
se_consumers['age_group'] = pd.cut(se_consumers['age'], bins=[15, 25, 35, 45, 60, 100],
                                   labels=['15-25', '26-35', '36-45', '46-60', '60+'])
print(f"\n  Age Distribution:")
for ag, cnt in se_consumers['age_group'].value_counts().sort_index().items():
    print(f"    {ag}: {cnt} consumers ({cnt/unique_consumers*100:.1f}%)")

# So sánh 4 quadrant
ne_n, se_n = len(nonstressed_engaged), len(stressed_engaged)
sd_n, nd_n = len(stressed_disengaged), len(nonstressed_disengaged)

print(f"\n  Cross-Comparison of 4 Quadrant Groups (Health cutoff=50, Engagement cutoff=median={eng_median:.1f}):")
print(f"    Non-Stressed & Engaged:      {ne_n:,} records ({nonstressed_engaged['consumer_id'].nunique()} unique)")
print(f"    Stressed & Engaged:          {se_n:,} records ({unique_consumers} unique)")
print(f"    Stressed & Disengaged:       {sd_n:,} records ({stressed_disengaged['consumer_id'].nunique()} unique)")
print(f"    Non-Stressed & Disengaged:   {nd_n:,} records ({nonstressed_disengaged['consumer_id'].nunique()} unique)")
print(f"    Total:                       {ne_n + se_n + sd_n + nd_n:,} records (= full dataset)")
print(f"    NOTE: A consumer may appear in multiple quadrants across different months.")

compare_metrics = ['financial_health_score', 'engagement_score', 'spend_to_income_ratio',
                   'credit_utilization_ratio', 'essential_spend_ratio', 'online_spend_ratio', 'spending_volatility']

print(f"\n    {'Metric':<30s} {'NonStr&Eng':>12s} {'Str&Eng':>12s} {'Str&Dis':>12s} {'NonStr&Dis':>12s}")
print(f"    {'-'*72}")
for m in compare_metrics:
    v1 = nonstressed_engaged[m].mean()
    v2 = stressed_engaged[m].mean()
    v3 = stressed_disengaged[m].mean()
    v4 = nonstressed_disengaged[m].mean()
    print(f"    {m:<30s} {v1:>12.3f} {v2:>12.3f} {v3:>12.3f} {v4:>12.3f}")

# Scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='engagement_score', y='financial_health_score',
                color=COLORS['neutral'], alpha=0.3, label='General Customers', s=20)
sns.scatterplot(data=stressed_engaged, x='engagement_score', y='financial_health_score',
                color=COLORS['negative'], label=f'Stressed & Engaged ({unique_consumers} consumers)', s=40)

plt.axvline(x=eng_median, color='gray', linestyle='--', linewidth=1.5,
            label=f'Engagement Median ({eng_median:.1f})')
plt.axhline(y=50, color='gray', linestyle='--', linewidth=1.5, label='Health Cutoff (50)')

# Label 4 góc
eng_right = (eng_median + 100) / 2
eng_left = eng_median / 2
plt.text(eng_right, 78, 'Non-Stressed &\nEngaged\n(Retention)', fontsize=9, alpha=0.6, ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
plt.text(eng_right, 22, f'Stressed &\nEngaged\n({unique_consumers} consumers)\n(Support Target)',
         fontsize=9, color=COLORS['negative'], fontweight='bold', ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
plt.text(eng_left, 78, 'Non-Stressed &\nDisengaged\n(Growth Opp.)', fontsize=9, alpha=0.6, ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
plt.text(eng_left, 22, 'Stressed &\nDisengaged\n(At-Risk)', fontsize=9, alpha=0.6, ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))

plt.title('3.4 Crossover Matrix: Engagement vs. Financial Health', fontweight='bold', fontsize=16, pad=20)
plt.xlabel('Engagement Score (Digital Interaction Level)')
plt.ylabel('Financial Health Score (Stability Indicator)')
plt.legend(loc='upper left', frameon=True)
plt.tight_layout(pad=2.0)
plt.savefig(os.path.join(CHART_DIR, "3_4_crossover_stressed_engaged.png"), dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "=" * 70)
print(f"All charts saved to: {os.path.abspath(CHART_DIR)}")
print("=" * 70)
