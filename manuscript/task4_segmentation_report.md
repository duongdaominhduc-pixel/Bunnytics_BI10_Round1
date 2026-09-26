# Phase 5: Customer Segmentation (Task 4) — Report for Slides

> **Role**: Business Intelligence Analyst  
> **Objective**: Segment the customer base into 6 actionable personas using a hybrid K-Means + Rule-Based approach, validated by Elbow Method and Silhouette Score.

---

## 1. Feature Engineering & Preprocessing

### Feature Selection (10 features from 3 numeric dimensions + demographics post-hoc)

| Dimension | Features Used | Count |
|-----------|--------------|-------|
| **Financial Health** | `financial_health_score`, `spend_to_income_ratio`, `credit_utilization_ratio`, `spending_volatility` | 4 |
| **Engagement** | `engagement_score`, `transaction_count`, `active_transaction_days` | 3 |
| **Spending Behavior** | `essential_spend_ratio`, `online_spend_ratio`, `category_diversity` | 3 |
| **Demographics** *(post-hoc profiling only)* | `age`, `gender`, `occupation`, `province_city` | — |

> **Why demographics are not used in K-Means**: Categorical variables (occupation, province) cannot be directly used in distance-based clustering without encoding that introduces arbitrary ordinal assumptions. Instead, we use them for **post-hoc profiling** to characterize discovered segments.

### Consumer-Level Aggregation

**Critical design decision**: The raw dataset contains 10,992 consumer-month rows (999 consumers × ~11 months). Clustering directly on consumer-month rows would allow a single customer to belong to **multiple clusters** across months — violating segmentation logic.

**Solution**: We aggregate to consumer-level by computing `mean()` across months for each feature, resulting in **999 unique consumer records**. This ensures each customer belongs to exactly one segment.

**Preprocessing**: Applied `StandardScaler` (mean=0, std=1) to prevent distance bias from differing scales.

---

## 2. Model Selection: K-Means + Rule-Based Hybrid

### Why K=6?
- **Business alignment**: The case study suggests 6 strategic personas. Using K=6 directly maps algorithmic output to business requirements.
- **Elbow Method**: Inertia shows diminishing returns after K=5–6.
- **Silhouette Score**: K=6 yields a Silhouette Score of **0.2167**. While moderate (typical for high-dimensional behavioral data with 10 features), this confirms that clusters are meaningfully separated rather than random.

### Why Hybrid (K-Means + Rule-Based)?
Pure K-Means assigns arbitrary cluster IDs (0, 1, 2...). A naive "pick the max/min" heuristic mapping can produce **misleading labels**. 

Our solution: Run K-Means first to discover natural data groupings, then apply **absolute threshold rules** on centroids (in priority order) to assign business-meaningful labels. This ensures every label is truthful relative to the data distribution and reproducible.

**Threshold Rules Applied (absolute thresholds, priority order):**
```
Rule 1: Disengaged (Healthy)     → engagement < 60 AND health ≥ 65
Rule 2: Disengaged (Vulnerable)  → engagement < 60 AND health < 65
Rule 3: Healthy & Engaged        → health ≥ 68 AND engagement ≥ 75
Rule 4: Stretched but Engaged    → health < 62 AND engagement ≥ 70
Rule 5: Emerging Digital          → engagement ≥ 78 AND volatility ≥ 1.8 AND txn_count ≥ median
Rule 6: Essential-Focused         → essential_spend_ratio ≥ 0.45 (catch remaining engaged clusters)
```

> **Why absolute thresholds?** With only K=6 centroids, relative percentile ranking (e.g., "top 20th percentile") is meaningless — a centroid at rank 2 of 6 is already at the 67th percentile. Absolute thresholds are interpretable and auditable.

---

## 3. The 6 Segment Profiles (Consumer-Level, n=999)

| # | Segment | Consumers | % | Health | Engage | Spend/Inc | Credit Util | Essential | Online | Volatility | Cat Div |
|---|---------|-----------|---|--------|--------|-----------|------------|-----------|--------|------------|---------|
| 1 | **Essential-Spend-Focused** | 288 | 28.8% | 66.3 | 76.7 | 0.729 | 0.197 | 0.473 | 0.204 | **1.353** | 13.6 |
| 2 | **Financially Healthy & Highly Engaged** | 245 | 24.5% | **71.5** | 78.2 | 0.531 | 0.135 | 0.490 | 0.202 | 1.493 | 13.8 |
| 3 | **Emerging Digital Customers** | 201 | 20.1% | 65.2 | **80.4** | 0.706 | 0.185 | 0.483 | 0.212 | **1.974** | **14.0** |
| 4 | **Financially Stretched but Highly Engaged** | 174 | 17.4% | **60.6** | 77.6 | **0.884** | **0.271** | 0.493 | 0.209 | 1.580 | 13.7 |
| 5 | **Low Engagement & Financially Vulnerable** | 52 | 5.2% | 61.0 | **50.8** | 0.701 | 0.210 | 0.112 | **0.703** | 0.657 | 5.0 |
| 6 | **Financially Healthy but Disengaged** | 39 | 3.9% | **71.7** | **45.8** | 0.509 | 0.130 | 0.211 | **0.588** | 0.722 | 4.8 |

### Detailed Persona Profiles, Demographics & Actions

**1. Essential-Spend-Focused Customers (28.8%)** — Largest segment
- *Behavioral Profile*: Moderate health (66.3), stable spending patterns (**lowest volatility** at 1.353). Spending concentrated on essential categories. Low online ratio (0.204).
- *Demographics*: Avg age **51.6** | Male 56.2% | Top provinces: TP.HCM (13.5%), Hà Nội (6.9%), Đồng Nai (5.9%)
- *Action*: **Value-Add Loyalty**. Partner with supermarkets/pharmacies for targeted cashback. Gently introduce digital features.

**2. Financially Healthy & Highly Engaged (24.5%)**
- *Behavioral Profile*: The "Golden Cohort." Highest health scores (71.5), balanced spending (spend/income=0.531), lowest credit utilization (0.135), and active digital users.
- *Demographics*: Avg age **52.2** | **Female-dominant** 55.5% | Top occupations: Engineers, Scientists | Top provinces: TP.HCM (15.9%), Hà Nội (13.1%)
- *Action*: **Retention Focus**. Offer premium digital rewards, exclusive features, and early access to new products.

**3. Emerging Digital Customers (20.1%)**
- *Behavioral Profile*: **Highest engagement** (80.4) and **highest spending volatility** (1.974) with the most diverse category usage (14.0 categories). Youngest segment. Below-average health (65.2) suggests they haven't yet mastered budgeting discipline.
- *Demographics*: Avg age **41.8** (youngest!) | **Female-dominant 60.7%** | Top provinces: TP.HCM (15.9%), Hà Nội (7.0%), Đồng Nai (6.5%)
- *Action*: **Nurture**. Deliver bite-sized financial literacy content via in-app stories. Deploy "Smart Budget" features prominently.

**4. Financially Stretched but Highly Engaged (17.4%)** — Highest-Risk segment
- *Behavioral Profile*: **Worst financial health** (60.6). Spend-to-income ratio of **0.884** signals near-overspending. **Highest credit utilization** (0.271). Yet they remain digitally active (engagement=77.6).
- *Demographics*: Avg age **49.6** | Male 56.3% | Top provinces: **Lâm Đồng** (7.5%), TP.HCM (6.3%), Thanh Hóa (5.2%) — more rural representation
- *Action*: **Immediate Non-Punitive Intervention**. Real-time spend alerts, automatic budget caps, and installment conversion programs. **Strictly avoid** credit limit reductions.

**5. Low Engagement & Financially Vulnerable (5.2%)**
- *Behavioral Profile*: **Lowest engagement** (50.8) among non-disengaged clusters. Extremely low essential spend (0.112) but **highest online ratio** (0.703). Very low category diversity (5.0) and low transaction frequency — they are "single-channel" digital users with limited interaction breadth.
- *Demographics*: Avg age **56.1** | Gender balanced 50/50 | Top provinces: TP.HCM (19.2%), Quảng Ngãi (9.6%)
- *Action*: **Multi-Channel Re-engagement**. Combine SMS/email outreach with app push notifications. Promote essential category spending and cross-category discovery.

**6. Financially Healthy but Disengaged (3.9%)** — Smallest segment
- *Behavioral Profile*: **Highest health** (71.7) but **lowest engagement** (45.8). High online spend ratio (0.588) but very low frequency (10 txn/month, 2 active days). They transact online but barely interact with the company's broader ecosystem.
- *Demographics*: **Oldest segment** avg age **61.5** | Gender balanced 51.3% Male | Top provinces: Lâm Đồng (12.8%), Cần Thơ (10.3%)
- *Action*: **Digital Onboarding**. Deploy targeted campaigns highlighting app features beyond payments (budget tracking, spending insights). Simplify UX for older users.

---

## 4. Post-Segmentation Comparison

### Visualizations (saved in `output/charts/`)

| Chart | File | Purpose |
|-------|------|---------|
| Elbow + Silhouette | `5_0_elbow_silhouette.png` | Justifies K=6 |
| Radar Chart | `5_1_segmentation_radar_chart.png` | Multi-dimensional centroid comparison |
| PCA Scatter Plot | `5_2_segmentation_pca_scatter.png` | 2D cluster separation visualization |
| Segment Size Bar | `5_3_segment_sizes.png` | Size distribution |
| **Heatmap** | `5_4_segment_heatmap.png` | Segment × metric normalized comparison |

### Key Behavioral Differences (Side-by-Side)

1. **Health vs. Engagement paradox**: The healthiest segment (Disengaged, 71.7) has the *lowest* engagement (45.8), while the most engaged (Emerging Digital, 80.4) has *below-average* health (65.2). This confirms health and engagement are **not linearly correlated**.

2. **Spending discipline spectrum**: Essential-Focused customers show the *lowest volatility* (1.353) → most stable spending. Emerging Digital shows the *highest* (1.974) → most erratic. This 46% volatility gap represents fundamentally different financial behaviors.

3. **Digital adoption gap**: At-Risk (online=0.703) and Disengaged (0.588) both have *high* online ratios but *low* engagement — they use online channels but don't interact broadly. In contrast, Healthy & Engaged (0.202) and Essential-Focused (0.204) have *low* online but *high* engagement — they prefer physical channels yet interact deeply.

---

## 5. Limitations & Future Work

**Limitations:**
- **Synthetic Data Caveat**: Absolute VND magnitudes are inflated. Cluster boundaries are driven by ratios, not real monetary thresholds. The "Disengaged" segments (39+52 consumers) are unusually small due to the simulation's inherently high engagement design.
- **Silhouette Score (0.22)**: Indicates moderate separation. Some clusters share overlapping behavioral profiles, reflecting the continuous nature of financial behavior rather than discrete archetypes.
- **Static Snapshot**: The current segmentation captures averaged behavior across months. Customers may migrate between segments over time (e.g., holiday spending in December could temporarily push "Healthy" customers into "Stretched").
- **No Demographics in Clustering**: Categorical variables (occupation, province) are excluded from K-Means. A future approach could use encoding techniques or mixed-type clustering (e.g., k-prototypes).

**Future Work:**
- **Customer Lifetime Value (CLV)**: Integrate predicted CLV as a segmentation dimension to prioritize high-value customer retention.
- **Segment Migration Tracking**: Implement a rolling 3-month re-clustering to identify customers transitioning between personas (early warning for deterioration).
- **DBSCAN for Outlier Isolation**: Before K-Means, apply density-based clustering to isolate extreme outlier behavior (potential fraud or default patterns).
- **Predictive Layer**: Combine segmentation with the `next_month_low_health_flag` model to predict which customers in the "Emerging Digital" or "At-Risk" segments are most likely to deteriorate next month.
- **Real-time Segmentation**: Deploy an online K-Means variant that updates segment assignments as new monthly data arrives, enabling dynamic intervention targeting.
