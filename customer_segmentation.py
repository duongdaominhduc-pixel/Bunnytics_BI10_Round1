import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Orange Concept Color Palette (extended for 6 clusters)
SEGMENT_COLORS = {
    'Essential-Spend-Focused Customers': '#FF8C00',
    'Financially Stretched but Highly Engaged': '#DC143C',
    'Financially Healthy & Highly Engaged': '#32CD32',
    'Financially Healthy but Disengaged': '#4682B4',
    'Emerging Digital Customers': '#FFD700',
    'At-Risk Transitional Customers': '#8A2BE2',
}

CHART_DIR = os.path.join(os.path.dirname(__file__), "output", "charts")
os.makedirs(CHART_DIR, exist_ok=True)

DATA_DIR = os.path.join(os.path.dirname(__file__), "ĐỀ BÀI", "DATASET")
df = pd.read_csv(os.path.join(DATA_DIR, "consumer_financial_health_engagement_2025.csv"))

print("=" * 70)
print("PHASE 5: CUSTOMER SEGMENTATION (K-MEANS + RULE-BASED HYBRID)")
print("=" * 70)

# =====================================================================
# 1. FEATURE ENGINEERING & PREPROCESSING
# =====================================================================
print("\n[1] FEATURE ENGINEERING & PREPROCESSING")

# --- Step 1a: Define clustering features from 3 numeric dimensions ---
# (Demographics are categorical → used for post-hoc profiling, not clustering)
cluster_features = [
    # Financial Health dimension
    'financial_health_score',
    'spend_to_income_ratio',
    'credit_utilization_ratio',
    'spending_volatility',
    # Engagement dimension
    'engagement_score',
    'transaction_count',
    'active_transaction_days',
    # Spending Behavior dimension
    'essential_spend_ratio',
    'online_spend_ratio',
    'category_diversity',
]

# Demographic features for post-hoc profiling
demo_features = ['age', 'gender', 'occupation', 'province_city']

print(f"  Clustering features ({len(cluster_features)} from 3 dimensions):")
print(f"    Financial Health: financial_health_score, spend_to_income_ratio, credit_utilization_ratio, spending_volatility")
print(f"    Engagement:       engagement_score, transaction_count, active_transaction_days")
print(f"    Spending:         essential_spend_ratio, online_spend_ratio, category_diversity")
print(f"  Demographics (post-hoc): age, gender, occupation, province_city")

# --- Step 1b: Aggregate consumer-month → consumer-level ---
print(f"\n  Aggregating {df.shape[0]:,} consumer-month rows → consumer-level (mean across months)...")

# Numeric aggregation
agg_dict = {feat: 'mean' for feat in cluster_features}
# Demographics: take first (static per consumer)
for d in demo_features:
    agg_dict[d] = 'first'

df_consumer = df.groupby('consumer_id').agg(agg_dict).reset_index()
print(f"  Result: {df_consumer.shape[0]:,} unique consumers")

# --- Step 1c: Scale ---
X = df_consumer[cluster_features].fillna(0)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(f"  Scaling: StandardScaler (mean=0, std=1)")

# =====================================================================
# 2. MODEL SELECTION — ELBOW + SILHOUETTE + K-MEANS
# =====================================================================
print("\n[2] MODEL SELECTION")

# 2a. Elbow Method
print("  Running Elbow Method (K=2..10)...")
inertias = []
sil_scores = []
K_range = range(2, 11)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels_k = km.fit_predict(X_scaled)
    inertias.append(km.inertia_)
    sil = silhouette_score(X_scaled, labels_k)
    sil_scores.append(sil)
    print(f"    K={k}: Inertia={km.inertia_:,.0f} | Silhouette={sil:.4f}")

# Elbow + Silhouette chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.plot(list(K_range), inertias, 'o-', color='#FF8C00', linewidth=2, markersize=8)
ax1.axvline(x=6, color='#DC143C', linestyle='--', label='K=6 (selected)')
ax1.set_title('Elbow Method: Inertia vs. K', fontweight='bold', pad=15)
ax1.set_xlabel('Number of Clusters (K)')
ax1.set_ylabel('Inertia (Within-Cluster Sum of Squares)')
ax1.legend()

ax2.plot(list(K_range), sil_scores, 'o-', color='#32CD32', linewidth=2, markersize=8)
ax2.axvline(x=6, color='#DC143C', linestyle='--', label='K=6 (selected)')
ax2.set_title('Silhouette Score vs. K', fontweight='bold', pad=15)
ax2.set_xlabel('Number of Clusters (K)')
ax2.set_ylabel('Silhouette Score')
ax2.legend()

plt.suptitle('Model Selection: Justifying K=6', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout(pad=2.0)
plt.savefig(os.path.join(CHART_DIR, "5_0_elbow_silhouette.png"), dpi=300, bbox_inches='tight')
plt.show()

# 2b. Final K-Means with K=6
print("\n  Running final K-Means (K=6) on consumer-level data...")
kmeans = KMeans(n_clusters=6, random_state=42, n_init=10)
df_consumer['cluster_id'] = kmeans.fit_predict(X_scaled)
final_sil = silhouette_score(X_scaled, df_consumer['cluster_id'])
print(f"  Final Silhouette Score: {final_sil:.4f}")
print(f"  Clustered {df_consumer.shape[0]:,} consumers (100% coverage)")

# =====================================================================
# 3. RULE-BASED LABEL MAPPING (ABSOLUTE THRESHOLDS)
# =====================================================================
print("\n[3] RULE-BASED LABEL MAPPING ON CENTROIDS")
centroids = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=cluster_features)
centroids['cluster_id'] = range(6)
centroids['size'] = df_consumer['cluster_id'].value_counts().sort_index().values

# Print raw centroids for transparency
print("\n  Raw Centroid Values:")
for _, row in centroids.iterrows():
    print(f"    Cluster {int(row['cluster_id'])} (n={int(row['size'])}): "
          f"Health={row['financial_health_score']:.1f} | "
          f"Engage={row['engagement_score']:.1f} | "
          f"Spend/Inc={row['spend_to_income_ratio']:.3f} | "
          f"CreditUtil={row['credit_utilization_ratio']:.3f} | "
          f"Essential={row['essential_spend_ratio']:.3f} | "
          f"Online={row['online_spend_ratio']:.3f} | "
          f"Volatility={row['spending_volatility']:.3f} | "
          f"TxnCount={row['transaction_count']:.0f} | "
          f"ActiveDays={row['active_transaction_days']:.0f} | "
          f"CatDiv={row['category_diversity']:.1f}")

# Rule-based mapping using RELATIVE centroid analysis
# (Consumer-level aggregation compresses value ranges, so we use relative
#  ranking across centroids rather than hard absolute thresholds)
def assign_label(row, all_centroids):
    h = row['financial_health_score']
    e = row['engagement_score']
    ess = row['essential_spend_ratio']
    onl = row['online_spend_ratio']
    si = row['spend_to_income_ratio']
    vol = row['spending_volatility']
    txn = row['transaction_count']

    # Compute relative ranks (percentiles within centroids)
    h_rank = (all_centroids['financial_health_score'] <= h).mean()
    e_rank = (all_centroids['engagement_score'] <= e).mean()

    # Rule 1: Disengaged — very low engagement (bottom of centroids)
    if e_rank <= 0.2:
        return "Financially Healthy but Disengaged"

    # Rule 2: Healthy & Engaged — highest health + good engagement
    if h_rank >= 0.8 and e_rank >= 0.5:
        return "Financially Healthy & Highly Engaged"

    # Rule 3: Stretched — worst health + highest spend-to-income among engaged clusters
    if h_rank <= 0.25 and si >= all_centroids['spend_to_income_ratio'].quantile(0.7):
        return "Financially Stretched but Highly Engaged"

    # Rule 4: Emerging Digital — very high engagement + high volatility/txn count
    if e_rank >= 0.8 and vol >= all_centroids['spending_volatility'].quantile(0.7):
        return "Emerging Digital Customers"

    # Rule 5: Essential-Focused — moderate-to-high essential ratio + lower volatility (stable spending)
    if ess >= all_centroids['essential_spend_ratio'].quantile(0.4) and h_rank >= 0.4 and vol <= all_centroids['spending_volatility'].median():
        return "Essential-Spend-Focused Customers"

    # Rule 6: At-Risk Transitional — everything else (moderate health, moderate engagement)
    return "At-Risk Transitional Customers"

centroids['segment_name'] = centroids.apply(lambda row: assign_label(row, centroids), axis=1)

# Map labels back to df_consumer
cluster_to_label = dict(zip(centroids['cluster_id'].astype(int), centroids['segment_name']))
df_consumer['segment_name'] = df_consumer['cluster_id'].map(cluster_to_label)

print("\n  Final Segment Mapping:")
for _, row in centroids.sort_values('financial_health_score', ascending=False).iterrows():
    print(f"    Cluster {int(row['cluster_id'])} -> {row['segment_name']}")
    print(f"      Health={row['financial_health_score']:.1f} | Engagement={row['engagement_score']:.1f} | Size={int(row['size'])}")

print("\n  Segment Distribution:")
seg_dist = df_consumer['segment_name'].value_counts()
for seg_name, cnt in seg_dist.items():
    print(f"    {seg_name}: {cnt} consumers ({cnt/len(df_consumer)*100:.1f}%)")

# Verify: check all 6 labels are assigned
assigned_labels = set(centroids['segment_name'])
expected_labels = set(SEGMENT_COLORS.keys())
missing = expected_labels - assigned_labels
if missing:
    print(f"\n  WARNING: Missing segments: {missing}")
else:
    print("\n  All 6 personas successfully mapped!")

# =====================================================================
# 4. DEMOGRAPHIC PROFILING PER SEGMENT
# =====================================================================
print("\n[4] DEMOGRAPHIC PROFILING PER SEGMENT")

for seg_name in seg_dist.index:
    seg_data = df_consumer[df_consumer['segment_name'] == seg_name]
    n = len(seg_data)
    print(f"\n  --- {seg_name} (n={n}, {n/len(df_consumer)*100:.1f}%) ---")

    # Age
    print(f"    Avg Age: {seg_data['age'].mean():.1f}")

    # Gender
    gender_dist = seg_data['gender'].value_counts(normalize=True) * 100
    gender_str = " | ".join([f"{g}: {p:.1f}%" for g, p in gender_dist.items()])
    print(f"    Gender: {gender_str}")

    # Top 3 occupations
    top_occ = seg_data['occupation'].value_counts().head(3)
    print(f"    Top 3 Occupations:")
    for occ, cnt in top_occ.items():
        print(f"      {occ}: {cnt} ({cnt/n*100:.1f}%)")

    # Top 3 provinces
    top_prov = seg_data['province_city'].value_counts().head(3)
    print(f"    Top 3 Provinces:")
    for prov, cnt in top_prov.items():
        print(f"      {prov}: {cnt} ({cnt/n*100:.1f}%)")

# =====================================================================
# 5. POST-SEGMENTATION COMPARISON (VISUALIZATION)
# =====================================================================
print("\n[5] GENERATING CHARTS...")

# Key display features for radar and heatmap (subset of cluster_features)
display_features = ['financial_health_score', 'engagement_score', 'spend_to_income_ratio',
                    'credit_utilization_ratio', 'essential_spend_ratio', 'online_spend_ratio',
                    'spending_volatility', 'category_diversity']

# --- 5A. SIDE-BY-SIDE COMPARISON TABLE ---
print("\n  Side-by-Side Comparison Table:")
comp_header = f"  {'Segment':<45s}"
for f in display_features:
    comp_header += f" {f[:12]:>12s}"
print(comp_header)
print("  " + "-" * (45 + 13 * len(display_features)))

for _, row in centroids.sort_values('financial_health_score', ascending=False).iterrows():
    line = f"  {row['segment_name']:<45s}"
    for f in display_features:
        line += f" {row[f]:>12.3f}"
    print(line)

# --- 5B. RADAR CHART ---
radar_features = ['financial_health_score', 'engagement_score', 'spend_to_income_ratio',
                  'credit_utilization_ratio', 'essential_spend_ratio', 'online_spend_ratio']

scaler_mm = MinMaxScaler()
radar_data = pd.DataFrame(scaler_mm.fit_transform(centroids[radar_features]), columns=radar_features)
radar_data['Segment'] = centroids['segment_name']

angles = np.linspace(0, 2 * np.pi, len(radar_features), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

for _, row in radar_data.iterrows():
    seg = row['Segment']
    values = row[radar_features].tolist()
    values += values[:1]
    color = SEGMENT_COLORS[seg]
    ax.plot(angles, values, color=color, linewidth=2, label=seg)
    ax.fill(angles, values, color=color, alpha=0.1)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(['Health\nScore', 'Engagement\nScore', 'Spend/\nIncome', 'Credit\nUtil', 'Essential\nRatio', 'Online\nRatio'], fontsize=11, fontweight='bold')
ax.set_yticks([])
plt.title('Post-Segmentation Comparison: 6 Persona Radar Profiles', size=16, fontweight='bold', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.45, 1.1), fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "5_1_segmentation_radar_chart.png"), dpi=300, bbox_inches='tight')
plt.show()

# --- 5C. HEATMAP: SEGMENT × METRIC ---
heatmap_data = centroids.set_index('segment_name')[display_features]
# Normalize per column (0-1) for comparable colors
heatmap_norm = (heatmap_data - heatmap_data.min()) / (heatmap_data.max() - heatmap_data.min())

plt.figure(figsize=(14, 7))
sns.heatmap(heatmap_norm, annot=heatmap_data.round(3).values, fmt='',
            cmap='YlOrRd', linewidths=1, linecolor='white',
            xticklabels=[f.replace('_', '\n') for f in display_features],
            yticklabels=heatmap_data.index, cbar_kws={'label': 'Normalized Value'})
plt.title('Segment × Metric Heatmap (values = actual centroid, colors = normalized)', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "5_4_segment_heatmap.png"), dpi=300, bbox_inches='tight')
plt.show()

# --- 5D. PCA SCATTER PLOT ---
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df_consumer['pca1'] = X_pca[:, 0]
df_consumer['pca2'] = X_pca[:, 1]

plt.figure(figsize=(12, 8))
for seg_name, color in SEGMENT_COLORS.items():
    mask = df_consumer['segment_name'] == seg_name
    if mask.sum() > 0:
        plt.scatter(df_consumer.loc[mask, 'pca1'], df_consumer.loc[mask, 'pca2'],
                    c=color, label=seg_name, s=30, alpha=0.6)

plt.title('K-Means Clusters (PCA 2D Projection) — Consumer Level', fontsize=16, fontweight='bold', pad=20)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)')
plt.legend(title='Customer Persona', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "5_2_segmentation_pca_scatter.png"), dpi=300, bbox_inches='tight')
plt.show()

# --- 5E. SEGMENT SIZE BAR CHART ---
seg_sizes = df_consumer['segment_name'].value_counts()
colors_ordered = [SEGMENT_COLORS[s] for s in seg_sizes.index]

plt.figure(figsize=(12, 6))
bars = plt.barh(seg_sizes.index, seg_sizes.values, color=colors_ordered)
for bar, val in zip(bars, seg_sizes.values):
    plt.text(val + 3, bar.get_y() + bar.get_height()/2,
             f'{val:,} ({val/len(df_consumer)*100:.1f}%)', va='center', fontweight='bold')
plt.title('Segment Size Distribution (Consumer-Level)', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Number of Unique Consumers')
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "5_3_segment_sizes.png"), dpi=300, bbox_inches='tight')
plt.show()

# =====================================================================
# 6. MAP SEGMENTS BACK TO ORIGINAL consumer-month DATA
# =====================================================================
# For downstream tasks that need consumer-month level data
consumer_segment_map = df_consumer.set_index('consumer_id')['segment_name'].to_dict()
df['segment_name'] = df['consumer_id'].map(consumer_segment_map)
print(f"\n[6] Mapped segments back to {len(df):,} consumer-month records (100% coverage)")
print(df['segment_name'].value_counts().to_string())

print("\n" + "=" * 70)
print(f"All charts saved to: {os.path.abspath(CHART_DIR)}")
print("=" * 70)
