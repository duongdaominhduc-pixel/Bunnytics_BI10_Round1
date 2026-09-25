"""Quick data loading & quality check script for BI10 datasets."""
import pandas as pd
import numpy as np
import sys
import os

DATA_DIR = r"d:\3. Research & Contest\BI10\PRELIMINARY PROJECT\ĐỀ BÀI\DATASET"

print("=" * 70)
print("LOADING DATASETS")
print("=" * 70)

# --- 1. Load consumer-month (small file first) ---
print("\n[1] Loading consumer_financial_health_engagement_2025.csv ...")
try:
    df_health = pd.read_csv(os.path.join(DATA_DIR, "consumer_financial_health_engagement_2025.csv"))
    print(f"    ✅ Success: {df_health.shape[0]:,} rows × {df_health.shape[1]} columns")
    print(f"    Memory: {df_health.memory_usage(deep=True).sum() / 1e6:.1f} MB")
except Exception as e:
    print(f"    ❌ Error: {e}")
    sys.exit(1)

# --- 2. Load transactions (large file — read first 100K for quick check) ---
print("\n[2] Loading consumer_transactions_2025.csv (first 100K rows for quick check) ...")
try:
    df_txn_sample = pd.read_csv(
        os.path.join(DATA_DIR, "consumer_transactions_2025.csv"),
        nrows=100_000
    )
    print(f"    ✅ Success: {df_txn_sample.shape[0]:,} rows × {df_txn_sample.shape[1]} columns")
except Exception as e:
    print(f"    ❌ Error: {e}")
    sys.exit(1)

# --- 3. Count total rows in transactions ---
print("\n[3] Counting total rows in transactions file ...")
total_txn = sum(1 for _ in open(os.path.join(DATA_DIR, "consumer_transactions_2025.csv"), encoding='utf-8')) - 1
print(f"    Total transactions: {total_txn:,}")

print("\n" + "=" * 70)
print("CONSUMER-MONTH DATASET (df_health)")
print("=" * 70)

# --- 4. Basic info ---
print("\n[4] Column Names & Data Types:")
for col in df_health.columns:
    null_count = df_health[col].isnull().sum()
    null_str = f" ⚠️ {null_count} nulls ({null_count/len(df_health)*100:.1f}%)" if null_count > 0 else ""
    print(f"    {col:45s} {str(df_health[col].dtype):12s}{null_str}")

# --- 5. Missing values ---
print(f"\n[5] Missing Values Summary:")
total_missing = df_health.isnull().sum().sum()
print(f"    Total missing cells: {total_missing}")
if total_missing > 0:
    missing = df_health.isnull().sum()
    for col in missing[missing > 0].index:
        print(f"    ⚠️ {col}: {missing[col]} missing ({missing[col]/len(df_health)*100:.1f}%)")
else:
    print("    ✅ No missing values!")

# --- 6. Duplicates ---
print(f"\n[6] Duplicate Check:")
dup_id_month = df_health.duplicated(subset=['consumer_id', 'analysis_month']).sum()
print(f"    (consumer_id, analysis_month) duplicates: {dup_id_month}")
if dup_id_month == 0:
    print("    ✅ No duplicates!")
else:
    print("    ⚠️ Duplicates found!")

# --- 7. Unique counts ---
print(f"\n[7] Key Unique Counts:")
print(f"    Unique consumers:      {df_health['consumer_id'].nunique()}")
print(f"    Unique months:         {df_health['analysis_month'].nunique()}")
print(f"    Rows (expected 999×12={999*12}): {len(df_health)}")
months_list = sorted(df_health['analysis_month'].unique())
print(f"    Months covered:        {months_list}")

# --- 8. Numeric describe ---
print(f"\n[8] Key Numeric Stats:")
key_cols = ['financial_health_score', 'engagement_score', 'total_spend_vnd',
            'spend_to_income_ratio', 'credit_utilization_ratio', 
            'essential_spend_ratio', 'online_spend_ratio', 'spending_volatility']
existing_cols = [c for c in key_cols if c in df_health.columns]
print(df_health[existing_cols].describe().round(4).to_string())

# --- 9. Segments distribution ---
print(f"\n[9] Segment Distributions:")
if 'financial_health_segment' in df_health.columns:
    print("    Financial Health Segments:")
    for seg, cnt in df_health['financial_health_segment'].value_counts().items():
        print(f"      {seg}: {cnt} ({cnt/len(df_health)*100:.1f}%)")
if 'engagement_segment' in df_health.columns:
    print("    Engagement Segments:")
    for seg, cnt in df_health['engagement_segment'].value_counts().items():
        print(f"      {seg}: {cnt} ({cnt/len(df_health)*100:.1f}%)")

# --- 10. Consistency checks ---
print(f"\n[10] Consistency Checks:")
# spend_amount >= 0
neg_spend = (df_health['total_spend_vnd'] < 0).sum()
print(f"    total_spend_vnd < 0: {neg_spend} {'✅' if neg_spend == 0 else '⚠️'}")

# financial_health_score range
fhs_min = df_health['financial_health_score'].min()
fhs_max = df_health['financial_health_score'].max()
print(f"    financial_health_score range: [{fhs_min:.1f}, {fhs_max:.1f}]")

# engagement_score range
es_min = df_health['engagement_score'].min()
es_max = df_health['engagement_score'].max()
print(f"    engagement_score range: [{es_min:.1f}, {es_max:.1f}]")

# Consumer consistency (same age, gender per consumer_id)
print(f"\n[11] Consumer-Level Consistency:")
consumer_age = df_health.groupby('consumer_id')['age'].nunique()
multi_age = (consumer_age > 1).sum()
print(f"    Consumers with multiple ages: {multi_age} {'✅' if multi_age == 0 else '⚠️'}")

consumer_gender = df_health.groupby('consumer_id')['gender'].nunique()
multi_gender = (consumer_gender > 1).sum()
print(f"    Consumers with multiple genders: {multi_gender} {'✅' if multi_gender == 0 else '⚠️'}")

consumer_occ = df_health.groupby('consumer_id')['occupation'].nunique()
multi_occ = (consumer_occ > 1).sum()
print(f"    Consumers with multiple occupations: {multi_occ} {'✅' if multi_occ == 0 else '⚠️'}")

print("\n" + "=" * 70)
print("TRANSACTIONS DATASET (sample — first 100K rows)")
print("=" * 70)

# --- 12. Transaction columns ---
print("\n[12] Column Names & Types:")
for col in df_txn_sample.columns:
    null_count = df_txn_sample[col].isnull().sum()
    null_str = f" ⚠️ {null_count} nulls" if null_count > 0 else ""
    print(f"    {col:35s} {str(df_txn_sample[col].dtype):12s}{null_str}")

# --- 13. Transaction duplicates ---
print(f"\n[13] Transaction ID Uniqueness (sample):")
dup_txn = df_txn_sample.duplicated(subset=['transaction_id']).sum()
print(f"    Duplicate transaction_id: {dup_txn} {'✅' if dup_txn == 0 else '⚠️'}")

# --- 14. Spend amount checks ---
print(f"\n[14] Spend Amount Checks (sample):")
neg = (df_txn_sample['spend_amount_vnd'] < 0).sum()
print(f"    spend_amount_vnd < 0: {neg} {'✅' if neg == 0 else '⚠️'}")
not_round = (df_txn_sample['spend_amount_vnd'] % 1000 != 0).sum()
print(f"    Not rounded to 1000 VND: {not_round} {'✅ All rounded' if not_round == 0 else '⚠️'}")
print(f"    Min: {df_txn_sample['spend_amount_vnd'].min():,.0f} VND")
print(f"    Max: {df_txn_sample['spend_amount_vnd'].max():,.0f} VND")
print(f"    Mean: {df_txn_sample['spend_amount_vnd'].mean():,.0f} VND")

# --- 15. Encoding check ---
print(f"\n[15] Vietnamese Encoding Check:")
sample_names = df_txn_sample['customer_name'].head(5).tolist()
print(f"    Sample names: {sample_names}")
sample_provinces = df_txn_sample['province_city'].unique()[:5].tolist()
print(f"    Sample provinces: {sample_provinces}")
sample_categories = df_txn_sample['spending_category'].unique().tolist()
print(f"    Categories ({len(sample_categories)}): {sample_categories}")
sample_channels = df_txn_sample['transaction_channel'].unique().tolist()
print(f"    Channels: {sample_channels}")

# --- 16. Date range ---
print(f"\n[16] Date Range (sample):")
dates = pd.to_datetime(df_txn_sample['activity_datetime'])
print(f"    Min: {dates.min()}")
print(f"    Max: {dates.max()}")

print("\n" + "=" * 70)
print("✅ DATA LOADING CHECK COMPLETE")
print("=" * 70)
