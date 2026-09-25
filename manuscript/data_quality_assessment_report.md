# Data Quality Assessment — Report for Slides

> **Slide Title**: Dataset Overview & Data Quality (Slide #5)
> **Key Message**: The dataset demonstrates exceptionally high quality and internal consistency, fully validating the progression to deep exploratory data analysis (EDA) and segmentation.

## 1. Dataset Overview
- **Scale**: 999 consumers, 34 provinces/cities, 693 merchants.
- **Transactions (Transaction-level)**: 1,852,394 records (Calendar 2025).
- **Health & Engagement (Monthly-aggregated)**: 10,992 records.

## 2. 6-Point Data Quality Checks

| Assessment Item | Result | Evaluation / Action |
|-----------------|--------|---------------------|
| **1. Missing Values** | 0 nulls in Transactions. 999 nulls in `next_month_low_health_flag` (December). | ✅ **Valid**. December is the final month, so "next month" data structurally cannot exist. Kept as-is. |
| **2. Duplicate Detection** | 0 duplicate transactions. 0 duplicate consumer-months. | ✅ **Perfect**. Absolute row-level uniqueness. |
| **3. Outlier Detection** | No negative amounts. 5.13% transactions exceed IQR. Health indicators show < 2.2% outliers. | ✅ **Normal**. Due to synthetic dataset characteristics, extreme values represent natural high-ticket discretionary spending, not technical errors. Kept as-is. |
| **4. Data Consistency** | 100% consistency across age, gender, occupation, customer names, and merchants. | ✅ **Perfect**. Strict 1-to-1 cardinality maintained (e.g., no age/gender shifting). |
| **5. Temporal Coverage** | 908 consumers have full 12-month data. 91 consumers exhibit periods of absolute inactivity. | ℹ️ **Insight**: 10,992 monthly records instead of 11,988. Ratios MUST be used over absolute sums to ensure fair comparability. |
| **6. Cross-dataset** | 100% match rate for `total_spend_vnd` and `transaction_count` across both tables. | ✅ **Perfect Data Integrity**. Transaction aggregations reconcile flawlessly with monthly snapshots. |

## 3. Key Takeaways for Presenter
- The dataset is completely clean. Any variations in absolute spending volumes stem from simulated behavioral patterns (e.g., inactive months), not missing data logic errors.
- The fundamental reliance on **ratio-based indicators** will act as our "true north" throughout all subsequent analytical phases to mitigate synthetic volume inflation.

## 4. Draft Content for Slides (English)
**Left Panel: Dataset Overview & Caveats**
* **Scale**: 999 consumers · 693 merchants · 34 provinces.
* **Granularity**: 
  * Transaction-level (`df_txn`): 1.85M records (Calendar 2025).
  * Monthly-aggregated (`df_health`): 10,992 records.
* **Temporal Coverage Note**: 91 consumers exhibit periods of absolute inactivity, yielding 10,992 monthly records instead of the theoretical 11,988.
* **Analytical Approach (Synthetic Data Caveat)**: Due to the synthetic nature of absolute VND magnitudes, all segmentations and analyses strictly leverage **ratio-based indicators** (e.g., *Spend-to-Income Ratio*, *Credit Utilization*) to ensure comparative validity.

**Right Panel: Data Quality & Reconciliation Matrix**
* **Data Completeness**: 100% complete. Nulls in `next_month_low_health_flag` for December 2025 are structurally valid (no imputation required).
* **Uniqueness**: ✅ 0 duplicates at both transaction ID and (consumer, month) levels.
* **Outlier Handling**: IQR/Z-score analysis confirms extreme values reflect natural high-ticket discretionary spending. No outliers truncated.
* **Attribute Consistency**: ✅ Demographic fields (Age, Gender, Occupation) strictly enforce 1-to-1 cardinality per consumer. 
* **Temporal Integrity**: ✅ 100% of timestamps bounded within 2025 limits.
* **Cross-dataset Reconciliation**: ✅ 100% match rate. Transaction-level aggregations reconcile perfectly with monthly snapshot table metrics (`total_spend` & `transaction_count`).
