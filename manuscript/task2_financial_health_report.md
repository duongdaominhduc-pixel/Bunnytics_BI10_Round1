# Phase 3: Financial Health Analysis (Task 2) — Report for Slides

> **Role**: Business Intelligence Analyst  
> **Guiding Principles**: (1) Rely on **ratio-based indicators** only (synthetic data caveat). (2) All interventions must be **ethical and non-punitive**.

---

## 3.1 Financial Health Score: Distribution & Trends
*(Addressing: "How healthy are customers financially?")*

**Verified Data Points:**
- **Mean score**: 66.37 | **Median**: 67.70 (right-skewed distribution — majority of customers are reasonably healthy).
- **Score range**: 0.80 – 90.20.
- **Risk zone** (score < 40): Only **95 records** (0.9% of all consumer-months).
- **Warning zone** (score < 50): **524 records** (4.8%).
- **Std**: 9.48 | **Skewness**: −0.916 (moderate left-skew — a long tail of financially stressed outliers pulling the distribution left).
- **Temporal trend**: The average score remains stable from January to November (~63–74). However, **December shows a sharp decline to 54.25**, likely driven by end-of-year holiday spending spikes that temporarily inflate the `spend_to_income_ratio`. This represents a **~14-point drop** from the annual average and highlights the need for proactive budget alerts before the holiday season.

**Key Takeaway**: The overwhelming majority of customers maintain scores above 60. However, a small but critical 4.8% are in the warning zone and require proactive support. The December deterioration signals a seasonal vulnerability window that the company should anticipate with pre-holiday financial wellness campaigns.

### Breakdown by Financial Health Segment

| Segment | Records | % of Total | Mean Score | Median Score |
|---------|---------|-----------|------------|-------------|
| Khỏe mạnh | 475 | 4.3% | 82.0 | 81.6 |
| Ổn định | 7,965 | 72.5% | 69.7 | 69.8 |
| Cần theo dõi | 2,457 | 22.4% | 53.9 | 54.4 |
| Có dấu hiệu căng thẳng tài chính | 95 | 0.9% | 29.1 | 34.3 |

**Insight**: The distribution is heavily right-skewed toward financial stability — **76.8%** of consumer-months fall into the top two segments (Khỏe mạnh + Ổn định). The "Cần theo dõi" segment (22.4%) represents the primary intervention target, while the critically stressed segment (0.9%) requires immediate, tailored support.

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
| 36–45 | 66.4 | 67.4 |
| 46–60 | 66.3 | 67.8 |
| 60+ | 66.9 | 68.6 |

**Finding**: Age has minimal impact on financial health scores (spread of only ~1.7 points across group means). However, the 15–25 cohort exhibits the **widest variance** (more extreme outliers below 40), suggesting younger customers are more prone to financial volatility despite similar median performance.

### Top 10 Occupations (by frequency)
| Occupation | Mean Score |
|-----------|-----------|
| Kỹ sư sản xuất (Manufacturing Engineer) | **71.9** (Highest) |
| Nhà khoa học thính học (Audiologist) | 71.2 |
| Kỹ sư vật liệu (Materials Engineer) | 71.1 |
| ... | ... |
| Biên tập viên chuyên đề tạp chí (Magazine Editor) | **63.3** (Lowest) |

**Finding**: An **8.5-point gap** separates the highest-scoring occupation (Manufacturing Engineers, 71.9) from the lowest (Magazine Editors, 63.3). Engineering and scientific professions consistently score higher, likely reflecting more stable income streams and disciplined spending patterns.

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
- **Health < 50**: We adopt 50 (rather than the dataset's built-in 40 threshold for `next_month_low_health_flag`) to capture not only currently distressed customers (score < 40, 0.9%) but also those in the **warning zone (40–50)** who are trending toward vulnerability. Combined, this represents the bottom **4.8%** of all consumer-months (524 records).
- **Engagement > 60**: Selected as the baseline for meaningful digital interaction. Given the dataset's inherently high engagement distribution (median = 78.1, a design characteristic noted in the case study), this threshold identifies customers who maintain at least moderate digital channel usage.

### Verified Segment Size
| Metric | Value |
|--------|-------|
| Consumer-month records | **520** |
| Unique consumers | **333** |
| % of total records | 4.7% |

### Customer Profile (Detailed)
These 333 consumers face immediate financial pressure yet demonstrate exceptional digital loyalty. Key metrics:

| Metric | Value (Segment Avg) | Overall Avg | Gap |
|--------|---------------------|-------------|-----|
| Financial Health Score | **43.83** | 66.37 | -22.5 |
| Engagement Score | **81.75** | ~78 | +3.8 |
| Spend-to-Income Ratio | **1.576** | ~0.98 | +60.8% higher |
| Credit Utilization | **0.459** | ~0.25 | +83.6% higher |
| Essential Spend Ratio | **0.341** | ~0.40 | -14.8% lower |
| Online Spend Ratio | **0.292** | ~0.28 | +4.3% higher |
| Spending Volatility | **2.814** | ~1.50 | +87.6% higher |

**Demographic highlights:**
- **Age skew**: 46–60 (31.8%) and 60+ (27.3%) dominate — older customers are over-represented, suggesting mid/late-career financial stress.
- **Top provinces**: TP. HCM (10.8%), Hà Nội (6.6%), Đồng Nai (5.4%), Cần Thơ (4.8%), Nghệ An (4.8%).
- **Occupations**: Highly fragmented (396 unique); no single occupation dominates, indicating this is a behavioral segment, not a demographic one.

### Cross-Comparison: 3 Quadrant Groups

| Metric | Healthy & Engaged (908 consumers) | Stressed & Engaged (333 consumers) | Stressed & Disengaged (4 consumers) |
|--------|:---:|:---:|:---:|
| Health Score | 70.4 | **43.8** | 40.8 |
| Engagement Score | 77.4 | **81.7** | 52.0 |
| Spend-to-Income | 0.566 | **1.576** (+178%) | 1.151 |
| Credit Utilization | 0.154 | **0.459** (+198%) | 0.350 |
| Essential Spend Ratio | 0.505 | **0.341** (−32%) | 0.225 |
| Online Spend Ratio | 0.194 | **0.292** (+51%) | 0.518 |
| Spending Volatility | 1.383 | **2.814** (+103%) | 1.768 |

**Key contrast**: The Stressed & Engaged group spends nearly **3× their income** compared to Healthy & Engaged peers, yet maintains **higher engagement** (81.7 vs 77.4). This paradox — financial distress combined with digital loyalty — makes them the ideal candidate for in-app intervention. The Stressed & Disengaged group is negligibly small (only 4 consumers), confirming that most financially stressed customers are actually highly digitally active.

### 🔥 Recommended Non-Punitive Strategies
*(Strictly avoid credit limit reductions or account suspensions)*
1. **Real-time Spend Alerts**: Deploy push notifications leveraging their high App engagement (e.g., *"You've reached 80% of your typical monthly discretionary budget"*).
2. **Proactive Budgeting Tools**: Surface "Smart Budget" or "Spending Goal" features on their App home screen.
3. **Installment Conversion**: Promote short-term installment plans for large transactions to alleviate immediate cash-flow pressure.
4. **Financial Literacy Content**: Deliver bite-sized educational content on spending discipline via in-app stories or notifications.
