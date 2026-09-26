# Phase 3: Financial Health Analysis (Task 2) — Report for Slides

> **Role**: Business Intelligence Analyst  
> **Guiding Principles**: (1) Rely on **ratio-based indicators** only (synthetic data caveat). (2) All interventions must be **ethical and non-punitive**.

---

## 3.1 Financial Health Score: Distribution & Trends
*(Addressing: "How healthy are customers financially?")*

**Verified Data Points:**
- **Mean score**: 66.37 | **Median**: 67.70 (**negatively skewed** distribution, skewness = −0.916 — a long tail of financially stressed outliers pulls the mean (66.37) below the median (67.70)).
- **Score range**: 0.80 – 90.20.
- **Risk zone** (score < 40): Only **95 records** (0.9% of all consumer-months).
- **Warning zone** (score < 50): **524 records** (4.8%).
- **Std**: 9.48 | **Skewness**: −0.916 (moderate left-skew — a long tail of financially stressed outliers pulling the distribution left).
- **Temporal trend**: The average score remains stable from January to November (~63–74). However, **December shows a sharp decline to 54.25**, likely driven by end-of-year holiday spending spikes that temporarily inflate the `spend_to_income_ratio`. This represents a **~13-point drop** from the January–November average (67.46) and highlights the need for proactive budget alerts before the holiday season.

**Key Takeaway**: The overwhelming majority of customers maintain scores above 60. However, a small but critical 4.8% are in the warning zone and require proactive support. The December deterioration signals a seasonal vulnerability window that the company should anticipate with pre-holiday financial wellness campaigns.

### Breakdown by Financial Health Segment

| Segment | Records | % of Total | Mean Score | Median Score |
|---------|---------|-----------|------------|-------------|
| Khỏe mạnh | 475 | 4.3% | 82.0 | 81.6 |
| Ổn định | 7,965 | 72.5% | 69.7 | 69.8 |
| Cần theo dõi | 2,457 | 22.4% | 53.9 | 54.4 |
| Có dấu hiệu căng thẳng tài chính | 95 | 0.9% | 29.1 | 34.3 |

**Insight**: The distribution is heavily concentrated toward financial stability — **76.8%** of consumer-months fall into the top two segments (Khỏe mạnh + Ổn định). The "Cần theo dõi" segment (22.4%) represents the primary intervention target, while the critically stressed segment (0.9%) requires immediate, tailored support.

---

## 3.2 Drivers of Low Financial Health (Correlation & Feature Importance)
*(Addressing: "Which factors drive low health?")*

Using both Pearson Correlation and Random Forest Feature Importance (n_estimators=100, random_state=42), we isolated the primary drivers:

| Rank | Feature | Correlation (r) | RF Importance |
|------|---------|-----------------|---------------|
| 1 | `spend_to_income_ratio` | **-0.8980** | **86.4%** |
| 2 | `credit_utilization_ratio` | **-0.8623** | 4.2% |
| 3 | `spending_volatility` | -0.4962 | 6.3% |
| 4 | `engagement_score` | -0.2990 | 0.5% |
| 5 | `online_spend_ratio` | -0.2731 | 0.6% |
| 6 | `essential_spend_ratio` | **+0.4806** | 2.0% |

**Interpretation:**
1. **Spend-to-Income Ratio** is the dominant predictor (r = -0.898, 86.4% importance). Customers who consistently overspend relative to their income capacity experience severe health score deterioration.
2. **Credit Utilization Ratio** acts as the secondary compounding factor (r = -0.862). High utilization signals liquidity stress.
3. **Spending Volatility** (6.3% importance) penalizes erratic month-over-month spending behavior, indicating lack of budgeting discipline.

💡 **Inverse Insight (Positive Signal)**: `essential_spend_ratio` exhibits a **positive** correlation (+0.481). Customers who allocate a larger proportion of spending to essential categories (groceries, healthcare, education) demonstrate fundamentally healthier financial profiles. This validates the intuition that disciplined, needs-based spending correlates with stability.

> **Note on Correlation vs. RF Importance ranking**: `credit_utilization_ratio` has the 2nd-highest |r| (0.862) but only 4.2% RF importance, while `spending_volatility` (|r| = 0.496) has 6.3%. This discrepancy arises from **multicollinearity**: `spend_to_income_ratio` and `credit_utilization_ratio` are highly correlated with each other, so the Random Forest assigns most importance to whichever feature it splits on first (spend_to_income, 86.4%), leaving little residual importance for credit_utilization. Correlation measures each feature's individual linear association independently.

### Partial Dependence Plots (Top 3 Drivers)

PDP analysis (via Random Forest) confirms the **non-linear** relationship between drivers and health score:

| Feature | PDP Pattern | Threshold Effect |
|---------|------------|------------------|
| `spend_to_income_ratio` | Sharp decline from 0→1.5, then flattens | Score collapses once ratio exceeds ~1.0 (spending > income) |
| `spending_volatility` | Gradual decline | Each unit increase in volatility costs ~3-5 health points |
| `credit_utilization_ratio` | Steep decline 0→0.5, then stabilizes | Utilization above 50% signals severe stress |

---

## 3.3 Demographic Differences (Occupation, Age, Province)
*(Addressing: "Where do spending habits differ by region, age, and occupation?")*

### Age Groups
| Age Group | Mean Score | Median Score |
|-----------|-----------|-------------|
| 15–25 | 65.2 | 66.9 |
| 26–35 | 66.2 | 67.2 |
| 36–45 | 66.4 | 67.3 |
| 46–60 | 66.3 | 67.8 |
| 60+ | 66.9 | 68.6 |

**Finding**: Age has minimal impact on financial health scores (spread of only ~1.7 points across group means). However, the 15–25 cohort exhibits the **widest variance** (more extreme outliers below 40), suggesting younger customers are more prone to financial volatility despite similar median performance.

### Top 10 Occupations (by frequency)
| Occupation | Mean Score |
|-----------|-----------|
| Kỹ sư sản xuất (Manufacturing Engineer) | **71.9** (Highest) |
| Nhà khoa học thính học (Audiologist) | 71.2 |
| Kỹ sư vật liệu (Materials Engineer) | 71.1 |
| Nhà khoa học y sinh (Biomedical Scientist) | 71.0 |
| Nhà địa chất hiện trường (Field Geologist) | 65.1 |
| Chuyên viên dựng phim (Film Editor) | 64.9 |
| Chuyên viên trắc địa (Surveyor) | 64.8 |
| Nhà thiết kế gốm sứ (Ceramic Designer) | 64.1 |
| Nhà trị liệu tâm lý trẻ em (Child Psychologist) | 64.0 |
| Biên tập viên chuyên đề tạp chí (Magazine Editor) | **63.3** (Lowest) |

**Finding**: An **8.6-point gap** separates the highest-scoring occupation (Manufacturing Engineers, 71.9) from the lowest (Magazine Editors, 63.3). A clear tier structure emerges: the top 4 (engineering and scientific professions) cluster tightly at 71.0–71.9, while the bottom 6 (creative and field professions) cluster at 63.3–65.1 — reflecting systematic differences in income stability and spending discipline.

### Top 5 Provinces (by customer count)
| Province | Mean Score | Median |
|----------|-----------|--------|
| Hà Nội | **68.0** | 69.6 |
| TP. Hồ Chí Minh | **67.9** | 69.0 |
| Cần Thơ | 66.9 | 68.0 |
| Đồng Nai | 66.2 | 67.2 |
| Lâm Đồng | **64.9** | 66.5 |

**Finding**: Contrary to the common assumption, **Tier-1 cities (Hanoi, HCMC) actually have higher health scores** (68.0, 67.9) compared to smaller provinces like Lâm Đồng (64.9). This 3.1-point gap may reflect higher income capacity in urban centers that offsets their elevated spending volumes.

### Statistical Significance (Kruskal-Wallis Tests)

| Grouping Variable | H-statistic | p-value | Significant? |
|---|---|---|---|
| Age groups | 26.81 | 2.17 × 10⁻⁵ | ✅ Yes |
| Occupations (Top 10) | 147.42 | 3.01 × 10⁻²⁷ | ✅ Yes |
| Provinces (Top 5) | 43.26 | 9.13 × 10⁻⁹ | ✅ Yes |

**Interpretation**: All three demographic dimensions show **statistically significant** differences in financial health score distributions (p < 0.001). Occupation exhibits by far the strongest effect (H=147.42), confirming that income stability and spending discipline vary meaningfully across professions.

---

## 3.4 Crossover Segment: Stressed × Engaged (Strategic Priority)
*(Addressing: "Which customers are highly engaged but financially stretched?")*

### Cutoff Justification
- **Health < 50** ("Stressed"): We adopt 50 (rather than the dataset's built-in 40 threshold for `next_month_low_health_flag`) to capture not only currently distressed customers (score < 40, 0.9%) but also those in the **warning zone (40–50)** who are trending toward vulnerability. Combined, this represents the bottom **4.8%** of all consumer-months (524 records).
- **Engagement > 78.1** (dataset median): Using the **median** as a data-driven, reproducible cutoff ensures a balanced split between engaged and disengaged populations. This avoids the pitfall of an arbitrary low threshold (e.g., 60, which would classify 99.2% of stressed records as "engaged" — rendering the comparison meaningless).

> **Note on labeling**: We use "Non-Stressed" (≥ 50) for the quadrant analysis below, distinct from "Khỏe mạnh" (≥ 80) used in section 3.1's four-tier segment classification. The lower cutoff captures the boundary between "warning zone" and "stable" customers for crossover analysis purposes.

### Verified Segment Size
| Metric | Value |
|--------|-------|
| Consumer-month records | **337** |
| Unique consumers | **255** |
| % of total records | 3.1% |

### Customer Profile (Detailed)
These 255 consumers face immediate financial pressure yet demonstrate above-median digital engagement. Key metrics:

| Metric | Value (Segment Avg) | Overall Avg | Gap |
|--------|---------------------|-------------|-----|
| Financial Health Score | **44.14** | 66.37 | −22.2 |
| Engagement Score | **86.27** | ~77.8 | +8.5 |
| Spend-to-Income Ratio | **1.565** | ~0.70 | +124% higher |
| Credit Utilization | **0.462** | ~0.19 | +143% higher |
| Essential Spend Ratio | **0.346** | ~0.48 | −28% lower |
| Online Spend Ratio | **0.383** | ~0.20 | +92% higher |
| Spending Volatility | **2.273** | ~1.51 | +50% higher |

**Demographic highlights:**
- **Age skew**: 46–60 (27.8%) and 60+ (28.2%) dominate — over half the segment consists of mid/late-career customers, suggesting financial stress peaks in the older cohorts.
- **Top provinces**: TP. HCM (11.0%), Hà Nội (5.9%), Đồng Nai (5.1%), Lâm Đồng (4.7%), Nghệ An (4.3%).
- **Occupations**: Highly fragmented (no single occupation exceeds 1.6%), confirming this is a **behavioral** segment, not a demographic one.

### Cross-Comparison: 4 Quadrant Groups

> **Unit**: Consumer-month records. A consumer may appear in multiple quadrants across different months (e.g., "Non-Stressed" in January but "Stressed" in December). All 10,992 records are accounted for with no overlap at the record level.

| Metric | Non-Stressed & Engaged (5,075 records) | Stressed & Engaged (337 records) | Stressed & Disengaged (187 records) | Non-Stressed & Disengaged (5,393 records) |
|--------|:---:|:---:|:---:|:---:|
| Health Score | 65.5 | **44.1** | 43.2 | 69.3 |
| Engagement Score | 82.1 | **86.3** | 73.0 | 73.4 |
| Spend-to-Income | 0.702 | **1.565** (+123%) | 1.588 | 0.612 |
| Credit Utilization | 0.189 | **0.462** (+144%) | 0.452 | 0.168 |
| Essential Spend Ratio | 0.461 | **0.346** (−25%) | 0.331 | 0.513 |
| Online Spend Ratio | 0.263 | **0.383** (+46%) | 0.133 | 0.152 |
| Spending Volatility | 1.604 | **2.273** (+42%) | **3.766** | 1.404 |

**Key contrasts:**
1. **Stressed & Engaged vs. Non-Stressed & Engaged**: Despite spending **2.2× their income** compared to stable peers (1.565 vs 0.702), the Stressed & Engaged group maintains **higher engagement** (86.3 vs 82.1). This paradox — financial distress combined with digital loyalty — makes them the ideal candidate for in-app intervention.
2. **Stressed & Disengaged** (187 records, 151 unique consumers): This group exhibits the **highest spending volatility** (3.766, nearly double that of Stressed & Engaged) but the **lowest online spend ratio** (0.133) — suggesting irregular, mostly offline spending patterns. They are harder to reach via digital channels and may require alternative outreach strategies (e.g., SMS, call center).
3. **Non-Stressed & Disengaged** (5,393 records, 945 unique consumers): The largest quadrant has the healthiest finances (69.3) but below-median engagement — representing a **growth opportunity** for digital channel adoption campaigns.

### 🔥 Recommended Non-Punitive Strategies
*(Strictly avoid credit limit reductions or account suspensions)*
1. **Real-time Spend Alerts**: Deploy push notifications leveraging their high App engagement (e.g., *"You've reached 80% of your typical monthly discretionary budget"*). **Target**: 255 Stressed & Engaged consumers.
2. **Proactive Budgeting Tools**: Surface "Smart Budget" or "Spending Goal" features on their App home screen. Their high online_spend_ratio (0.383 vs 0.20 overall) confirms frequent digital channel usage.
3. **Installment Conversion**: Promote short-term installment plans for large transactions to alleviate immediate cash-flow pressure (spend_to_income = 1.565, credit utilization = 0.462).
4. **Financial Literacy Content**: Deliver bite-sized educational content on spending discipline via in-app stories or notifications. Priority demographic: 46–60 and 60+ age cohorts (56.0% of segment).
5. **December Pre-Holiday Alerts**: Deploy proactive budget reminders in November, targeting the ~13-point December score decline identified in section 3.1.
