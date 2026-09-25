# 📑 BI10 Round 01 — Slide Proposal Outline (v2)
## [TeamName_LeaderName_BI10_R01]

> **Format**: 16:9 · Max 22 slides · English · Max 100 MB  
> **Sections**: Cover → Executive Summary → TOC → Introduction → Tasks 1–5 → Closing

---

## Slide Allocation (22/22)

| # | Section | Slide Title |
|---|---------|-------------|
| 1 | **Cover** | Cover Page |
| 2 | **Executive Summary** | Executive Summary |
| 3 | **Table of Contents** | Table of Contents |
| 4 | **Introduction** | Business Context & Objectives |
| 5 | **Introduction** | Dataset Overview & Data Quality |
| 6 | **Task 1** | Q1 — Peak Spending Month |
| 7 | **Task 1** | Q2 — Regional Digital Adoption Gaps |
| 8 | **Task 1** | Q3 & Q4 — Category & Age Cohort Analysis |
| 9 | **Task 1** | Spending Decomposition & Business Drivers |
| 10 | **Task 2** | Financial Health Score Distribution |
| 11 | **Task 2** | Drivers of Low Health & Demographic Differences |
| 12 | **Task 2** | Crossover — Stressed × Highly Engaged |
| 13 | **Task 3** | Engagement Distribution & Channel Adoption |
| 14 | **Task 3** | Diversity, Recency, Frequency & Healthy-but-Disengaged |
| 15 | **Task 4** | Feature Engineering & Preprocessing |
| 16 | **Task 4** | Model Selection & Validation |
| 17 | **Task 4** | 6 Segment Profiles |
| 18 | **Task 4** | Post-Segmentation Comparison & Limitations |
| 19 | **Task 5** | 6 Non-Punitive Interventions |
| 20 | **Task 5** | Prioritisation & Ethical Framework |
| 21 | **Closing** | Key Takeaways |
| 22 | **Closing** | Thank You & Contact |

```mermaid
flowchart LR
    S1["#1\nCover"] --> S2["#2\nExec Summary"]
    S2 --> S3["#3\nTOC"]
    S3 --> S4["#4–5\nIntroduction"]
    S4 --> T1["#6–9\nTask 1\nEDA"]
    T1 --> T2["#10–12\nTask 2\nHealth"]
    T2 --> T3["#13–14\nTask 3\nEngagement"]
    T3 --> T4["#15–18\nTask 4\nSegmentation"]
    T4 --> T5["#19–20\nTask 5\nRecommend"]
    T5 --> CL["#21–22\nClosing"]

    style S1 fill:#0f172a,stroke:#f8fafc,color:#f8fafc
    style S2 fill:#1e293b,stroke:#38bdf8,color:#f8fafc
    style S3 fill:#1e293b,stroke:#38bdf8,color:#f8fafc
    style S4 fill:#1e293b,stroke:#64748b,color:#f8fafc
    style T1 fill:#064e3b,stroke:#10b981,color:#f8fafc
    style T2 fill:#7f1d1d,stroke:#ef4444,color:#f8fafc
    style T3 fill:#3b0764,stroke:#a855f7,color:#f8fafc
    style T4 fill:#831843,stroke:#ec4899,color:#f8fafc
    style T5 fill:#0c4a6e,stroke:#06b6d4,color:#f8fafc
    style CL fill:#0f172a,stroke:#f8fafc,color:#f8fafc
```

---

## SLIDE-BY-SLIDE DETAIL

---

### Slide #1 — Cover Page 🆕

**Title**: Consumer Financial Health & Engagement

**Content**:

| Element | Detail |
|---------|--------|
| **Competition** | BI10 — Preliminary Round 01 |
| **Project Title** | Consumer Financial Health & Engagement: Understanding Spending Behaviour and Building Meaningful Customer Segments |
| **Team Name** | [TeamName] |
| **Members** | [Name 1 — Leader] · [Name 2] · [Name 3] · ... |
| **University** | [University Name] |
| **Date** | [Submission Date] |

**Visual**: Full-bleed gradient or themed background with team/university logo. Clean, professional, impactful first impression.

---

### Slide #2 — Executive Summary

**Title**: Executive Summary

**Content** (concise 1-page overview — write this LAST):

| Block | Content |
|-------|---------|
| **Context** | ITB is shifting from reactive collections to proactive financial wellbeing |
| **Data** | 999 consumers · 1.85M transactions · 34 provinces · 2025 (synthetic) |
| **Finding 1** | Peak spending: Month X = ₫Y billion (Z% of annual) |
| **Finding 2** | Top drivers of low financial health: [ratio 1], [ratio 2] |
| **Finding 3** | Crossover segments identified: N stressed-but-engaged + M healthy-but-disengaged |
| **Finding 4** | 6 data-driven customer segments built and validated |
| **Action** | 6 non-punitive interventions proposed, ranked by reach × driver strength |
| **Ethical rule** | `financial_health_score` ≠ credit score — never for credit denial |

**Visual**: Hero KPI strip (4–5 key numbers with icons) across the top

> [!TIP]
> Viết slide này **cuối cùng** sau khi phân tích xong, để số liệu chính xác.

---

### Slide #3 — Table of Contents

**Title**: Table of Contents

```
1. Introduction
   1.1 Business Context & Objectives .......................... Slide 4
   1.2 Dataset Overview & Data Quality ........................ Slide 5

2. Analysis Results
   Task 1 — Exploratory Data Analysis ......................... Slides 6–9
   Task 2 — Financial Health Analysis ......................... Slides 10–12
   Task 3 — Customer Engagement Analysis ...................... Slides 13–14
   Task 4 — Customer Segmentation ............................. Slides 15–18
   Task 5 — Business Recommendations .......................... Slides 19–20

3. Closing
   Key Takeaways .............................................. Slide 21
   Thank You & Contact ........................................ Slide 22
```

**Visual**: Numbered list with color-coded section markers. Keep clean and scannable.

---

### Slide #4 — Business Context & Objectives

**Title**: Business Context & Analytical Objectives

**Content**:

| Block | What to write |
|-------|---------------|
| **Company** | ITB — Vietnamese consumer-finance company (cards & short-term credit) |
| **Strategic shift** | Reactive collections → **proactive financial wellbeing** |
| **6 Core questions** | ① How healthy are customers? What drives low health? ② How engaged are they with channels? Who is drifting? ③ Where do spending habits differ (region, age, occupation)? ④ Who is healthy-but-disengaged? (growth opportunity) ⑤ Who is stretched-but-engaged? (support opportunity) ⑥ How to segment & design non-punitive interventions? |
| **Ethical constraint** | ⚠️ `financial_health_score` is a wellbeing indicator — **NEVER** for credit decisions |

**Visual**: Icon strip for 6 questions on the right; company context on the left

---

### Slide #5 — Dataset Overview & Data Quality

**Title**: Dataset Overview & Data Quality Summary

**Left panel — Datasets**:

| Dataset | Grain | Rows | Cols |
|---------|-------|------|------|
| `consumer_transactions_2025` | 1 row / txn | 1,852,394 | 28 |
| `consumer_financial_health_engagement_2025` | 1 row / consumer / month | 10,992 | 30 |

- 999 consumers · 693 merchants · 34 provinces · Calendar 2025
- Monetary unit: VND — **ratios are the reliable signal** (synthetic data)

**Right panel — Quality Checks**:

| Check | Status |
|-------|--------|
| Missing values | _[fill]_ |
| Duplicate `transaction_id` | ✅ 0 |
| `(consumer, month)` unique | ✅ |
| `spend_amount_vnd` ≥ 0 & mod 1000 = 0 | ✅ |
| All timestamps ∈ 2025 | ✅ |
| Cross-dataset consistency (txn ↔ monthly) | _[fill: match %]_ |
| Synthetic caveat | Acknowledged |

**Visual**: Two-column layout — data schema left, checklist right

---

## ═══ TASK 1: EXPLORATORY DATA ANALYSIS (Slides 6–9) ═══

---

### Slide #6 — Q1: Peak Spending Month

**Title**: Q1 — Which Month Records the Highest Total Spend?

**Content**:
- **Bar chart**: Total monthly spend (VND) for 12 months — highlight peak
- **Callout**: "**Month X** = ₫Y billion, accounting for **Z%** of annual spend"
- Decomposition: peak driven by more transactions or higher ticket sizes?
- Essential vs. Discretionary split for peak month vs. average

**Required output**: Exact VND figure + % of annual spend

**Chart**: Vertical bar chart (12 bars) with average line + peak annotation

---

### Slide #7 — Q2: Regional Digital Adoption Gaps

**Title**: Q2 — High-Spend Provinces with Low Digital Transaction Share

**Content**:
- Identify **≥ 2 provinces**: high total spend BUT `digital_share < national average`
- Channel breakdown: POS vs. E-commerce vs. QR vs. Mobile App vs. Recurring
- National avg digital share as benchmark line
- Business insight: opportunity for digital-channel nudges in these hubs

**Required output**: Province names, spend volumes, digital shares, channel comparison

**Chart**: Grouped horizontal bar chart — channel mix per province + national benchmark

---

### Slide #8 — Q3 & Q4: Categories & Age Cohort *(merged)* 🔀

**Title**: Category Performance & Age Cohort Financial Vulnerability

**Layout**: Split slide — left half Q3, right half Q4

**Left half — Q3: Top Categories**:
- **Top by transaction count**: [Category A] — N txns, avg ticket ₫X
- **Top by total spend**: [Category B] — ₫Y total, avg ticket ₫Z
- Compare average ticket sizes
- Insight: high-frequency-low-value vs. low-frequency-high-value

**Right half — Q4: Age Cohort Vulnerability**:
- Age cohorts: 18–25 / 26–35 / 36–45 / 46–55 / 56+
- Identify cohort with **active frequency + lowest avg `financial_health_score`**
- Key metrics: `essential_spend_ratio`, `spend_to_income_ratio`
- Insight: why this cohort is financially vulnerable

**Charts**: Bubble chart or dual bar (left) · Grouped bar or radar (right)

> [!NOTE]
> Merging Q3 & Q4 vào 1 slide vì cả hai đều phân tích "so sánh metrics giữa segments". Dùng split-layout 50/50 để giữ clarity.

---

### Slide #9 — Spending Decomposition & Business Drivers

**Title**: Spending Structure — Seasonality, Drivers & Decomposition

**Content**:
- **Stacked area chart**: Essential vs. Discretionary spending over 12 months
- **Decomposition**: Transaction volume effect vs. ticket size effect on peak month
- Top-performing vs. lagging regional + channel segments
- Business interpretations: behavioral patterns, risk/opportunity drivers

**Required output**: Driver decomposition, top/lagging segments, business narrative

**Chart**: Stacked area (main) + waterfall decomposition (inset) + key insight callouts

---

## ═══ TASK 2: FINANCIAL HEALTH ANALYSIS (Slides 10–12) ═══

---

### Slide #10 — Financial Health Score Distribution

**Title**: Financial Health Score — Distribution & Trends

**Content**:
- **Histogram + KDE** of `financial_health_score` (all consumer-months)
- Summary: mean, median, std, skewness
- **Segment share**: donut chart → % in each `financial_health_segment`
- **Monthly trend**: line sparkline — does health improve or worsen over the year?

**Constraint**: Ratio-based fields only. All claims backed by numbers/charts.

**Chart**: Histogram+KDE (center) · segment donut (top-right) · monthly trend sparkline (bottom)

---

### Slide #11 — Drivers of Low Health & Demographic Differences *(merged)* 🔀

**Title**: What Drives Low Financial Health? — Factor Analysis & Demographics

**Layout**: 60% left (drivers) + 40% right (demographics)

**Left — Top Drivers**:
- Feature importance bar chart (from RF/XGBoost regressor):
  - `spend_to_income_ratio`, `credit_utilization_ratio`, `spending_volatility`, `essential_spend_ratio`, `online_spend_ratio`
- Key insight: "Customers with `spend_to_income > X` and `credit_util > Y` are Z× more likely to score < 40"

**Right — Demographic Breakdown**:
- Box plot: health score by **occupation** (top 5–6)
- Grouped bar: avg health by **age cohort**
- Horizontal bar: avg health by **province** (top 8)
- Highlight most/least healthy groups

**Charts**: Horizontal importance bars (left) · compact box/bar plots (right, stacked vertically)

> [!NOTE]
> Merging drivers + demographics saves 1 slide. Use a 60/40 split — drivers as the "hero" analysis, demographics as supporting evidence.

---

### Slide #12 — Crossover: Financially Stressed × Highly Engaged

**Title**: Crossover Segment — Financially Stressed but Highly Engaged

**Content**:
- **Rule** (clear, reproducible):
  - e.g., `financial_health_score < 40` AND `engagement_score ≥ 70`
- **Size**: N customers (X% of total 999)
- **Profile table**:

| Attribute | Crossover Segment | Overall Average |
|-----------|-------------------|-----------------|
| Avg age | _?_ | _?_ |
| Top occupation | _?_ | _?_ |
| Top province | _?_ | _?_ |
| essential_spend_ratio | _?_ | _?_ |
| spend_to_income_ratio | _?_ | _?_ |
| credit_utilization | _?_ | _?_ |

- **Business framing**: Active customers in need → support, don't punish

**Chart**: Scatter plot (health × engagement) with quadrant shading + profile table

---

## ═══ TASK 3: CUSTOMER ENGAGEMENT ANALYSIS (Slides 13–14) ═══

---

### Slide #13 — Engagement Distribution & Channel Adoption

**Title**: Engagement Score Distribution & Channel Mix

**Left — Engagement Distribution**:
- Histogram of `engagement_score`
- Share (%) in each `engagement_segment` — donut or stacked bar

**Right — Channel Adoption**:
- Breakdown: POS / QR / E-commerce / Mobile App / Recurring
- % of spend that is digital vs. offline
- Monthly digital share trend (optional sparkline)

**Required deliverables**: ① Engagement distribution + segment share ② Channel adoption (5 channels)

**Chart**: Histogram + donut (left) · stacked bar or treemap (right)

---

### Slide #14 — Diversity, Recency, Frequency & Healthy-but-Disengaged *(merged)* 🔀

**Title**: Category Diversity, Recency & Frequency — and the Retention-Risk Segment

**Layout**: Top 60% (metrics) + Bottom 40% (crossover segment)

**Top — Engagement Metrics**:
- `category_diversity` ↔ `engagement_score`: scatter + Pearson/Spearman r
- `transaction_recency_days` distribution: high recency = churn risk
- `transaction_count` / `active_transaction_days` ↔ engagement: scatter

**Bottom — Healthy but Disengaged Segment**:
- **Cutoff**: `financial_health_score ≥ 70` AND `engagement_score < 40`
- **Justification**: why not stricter (≥80, <30) or looser (≥60, <50)?
- **Size**: N customers (X%)
- **Quick profile**: demographics, channels, avg recency
- **Framing**: Good customers drifting away → retention & growth opportunity

**Charts**: Mini scatter grid (top) · scatter quadrant with highlight + profile card (bottom)

> [!NOTE]
> Nén 2 slides thành 1 bằng top/bottom layout. Top phần metrics dùng mini scatter grid (3 cái nhỏ cạnh nhau), bottom highlight crossover segment.

---

## ═══ TASK 4: CUSTOMER SEGMENTATION (Slides 15–18) ═══

---

### Slide #15 — Feature Engineering & Preprocessing

**Title**: Segmentation — Data Preprocessing & Feature Engineering

**Content**:

| Dimension | Features |
|-----------|----------|
| **Demographics** | age, gender, occupation, province_city |
| **Financial Health** | financial_health_score, credit_utilization_ratio, spend_to_income_ratio, spending_volatility |
| **Engagement** | engagement_score, transaction_count, active_transaction_days, transaction_recency_days |
| **Spending Behavior** | essential_spend_ratio, discretionary_spend_ratio, online_spend_ratio, category_diversity |

- Aggregation: consumer-month → **consumer-level** (mean/median across 12 months)
- Scaling: StandardScaler on all numeric features
- Additional engineered ratios (if any)

**Chart**: Pipeline flowchart (raw → aggregate → scale → model) + correlation heatmap

---

### Slide #16 — Model Selection & Validation

**Title**: Segmentation Model — Methodology & Validation

**Content**:
- **Approach**: K-Means / GMM / Rule-Based / Hybrid (justify choice)
- If clustering:
  - Elbow plot → optimal k
  - Silhouette score comparison
  - PCA 2D scatter colored by cluster
- If rule-based:
  - Decision matrix logic
  - Coverage: 100% customers assigned
- Validation metrics: silhouette, calinski-harabasz, distribution balance

**Chart**: Elbow + silhouette plots (top) · PCA 2D scatter (bottom) or rule matrix diagram

---

### Slide #17 — 6 Segment Profiles

**Title**: Customer Segments — Profiles & Key Differentiators

**Content**:

| Segment | Size | Health | Engagement | Defining Trait |
|---------|------|--------|-----------|----------------|
| 🟢 Healthy & Highly Engaged | n (x%) | High | High | Ideal customers |
| 🔵 Healthy but Disengaged | n (x%) | High | Low | Retention risk |
| 🟠 Stretched but Engaged | n (x%) | Low | High | Need support |
| 🔴 Vulnerable & Disengaged | n (x%) | Low | Low | Highest risk |
| 💜 Emerging Digital | n (x%) | Varies | Varies | High online ratio |
| ⚪ Essential-Focused | n (x%) | Varies | Varies | High essential ratio |

- **Radar chart**: 6 segments overlaid on 5–6 key metrics
- Key differentiating attributes highlighted per segment

**Chart**: Summary table + radar/spider chart (6 polygons)

---

### Slide #18 — Post-Segmentation Comparison & Limitations

**Title**: Segment Comparison, Limitations & Future Work

**Top — Heatmap Comparison**:
- Heatmap: segment × metric (health, engagement, spend_to_income, online_ratio, category_diversity, credit_util)
- Key behavioral differences highlighted
- 1-line business implication per segment

**Bottom — Limitations & Future Work**:
- ⚠️ Synthetic data: income/credit magnitudes unrealistic → ratios used
- ⚠️ Engagement skews high → differentiation via digital adoption & category diversity
- 🔮 Future: real data validation, temporal stability check, CLV integration, real-time segmentation, churn prediction

**Chart**: Heatmap (top 60%) + bullet list (bottom 40%)

---

## ═══ TASK 5: BUSINESS RECOMMENDATIONS (Slides 19–20) ═══

---

### Slide #19 — 6 Non-Punitive Interventions

**Title**: Non-Punitive Action Plan — 6 Data-Driven Interventions

| # | Intervention Type | Target Group | Data Evidence | Reach |
|---|-------------------|-------------|---------------|-------|
| 1 | 🛠️ **Budgeting Tools** | High `spend_to_income_ratio` (Stretched segment) | _[column + value]_ | n (x%) |
| 2 | 🔔 **Spend Alerts** | High `spending_volatility` customers | _[column + value]_ | n (x%) |
| 3 | 📅 **Financial-Planning Reminders** | Young cohort (18–30) with low health | _[column + value]_ | n (x%) |
| 4 | 📚 **Financial-Education Content** | Vulnerable segment | _[column + value]_ | n (x%) |
| 5 | 📱 **Digital-Channel Nudges** | Low digital-share provinces (from Q2) | _[column + value]_ | n (x%) |
| 6 | 💳 **Product Suggestions** | Healthy+Engaged (upsell) / Emerging Digital (cross-sell) | _[column + value]_ | n (x%) |

> [!CAUTION]
> **Credit Rule**: `financial_health_score` must **NEVER** be used to deny credit, reduce limits, or block accounts.

**Chart**: Icon table with reach sparklines per row

---

### Slide #20 — Prioritisation & Ethical Framework

**Title**: Intervention Prioritisation & Ethical Commitment

**Top — Priority Ranking**:

| Rank | Intervention | Reach | Driver Strength | Effort |
|------|-------------|-------|----------------|--------|
| 1 | _[highest impact]_ | _n_ | ★★★ | Low |
| 2 | ... | ... | ★★★ | Med |
| ... | ... | ... | ... | ... |
| 6 | _[lowest priority]_ | _n_ | ★ | High |

Or: **Bubble chart** (x = reach, y = driver strength, size = implementation effort)

**Bottom — Ethical Commitment**:
- ✅ All interventions are **supportive, not punitive**
- ✅ No credit denials, limit cuts, or account blocks based on `financial_health_score`
- ✅ Fairness audit: no disproportionate disadvantage by region, age, or occupation
- ✅ Synthetic data discipline = production data discipline

**Chart**: Bubble/matrix chart (top) · commitment checklist with checkmarks (bottom)

---

## ═══ CLOSING (Slides 21–22) ═══ 🆕

---

### Slide #21 — Key Takeaways

**Title**: Key Takeaways

**Content**: 5–6 bullet points summarising the entire analysis:

| # | Takeaway |
|---|----------|
| 1 | **Seasonal spending** peaks in Month X, driven by [volume/ticket size] |
| 2 | **Low financial health** is primarily driven by `spend_to_income_ratio` and `credit_utilization_ratio` |
| 3 | **N customers** are stretched-but-engaged — they need support, not punishment |
| 4 | **M customers** are healthy-but-disengaged — a retention/growth opportunity worth pursuing |
| 5 | **6 actionable segments** enable targeted, data-driven, ethical interventions |
| 6 | **Every recommendation** is grounded in data and respects the non-punitive principle |

**Visual**: Large numbered list with icons · Optional: 3 hero metric callouts across the top

---

### Slide #22 — Thank You & Contact 🆕

**Title**: Thank You

**Content**:
- **Team Name**: [TeamName]
- **Members**: [Full names + roles]
- **University**: [University Name]
- **Contact**: [Email / Phone / LinkedIn]
- **Tagline**: *"From data to wellbeing — supporting customers, not punishing them."*

**Visual**: Clean, professional closing slide matching the cover design. Team/university logo. Gradient background.

---

## 🎨 Design System

### Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| Primary | `#1E3A5F` | Titles, headers, cover |
| Accent 1 | `#00B4D8` | Charts primary, highlights |
| Accent 2 | `#FF6B35` | Warnings, callouts, emphasis |
| Positive | `#06D6A0` | Healthy / positive |
| Negative | `#EF476F` | Stretched / negative |
| Neutral | `#8B95A5` | Supporting text, dividers |
| Background | `#F8F9FA` | Slide background |
| Dark BG | `#0F172A` | Cover & closing slides |

### Typography
- **Titles**: Montserrat Bold, 28–32pt
- **Subtitles**: Montserrat Semi-Bold, 20–24pt
- **Body**: Inter Regular, 14–18pt
- **Chart labels**: Inter, 10–12pt

### Chart Rules
- Every chart: clear title + axis labels + unit (VND / % / count)
- Consistent segment colors across ALL slides
- Annotate key data points directly on charts
- Source note: *"Source: Synthetic data — ITB Consumer Finance, 2025"*

---

## 📋 Deliverable Traceability Matrix

| Requirement (from đề bài) | Slide # |
|---------------------------|---------|
| Cover page | **#1** |
| Executive Summary | **#2** |
| Table of Contents | **#3** |
| Business Context & Objectives | **#4** |
| Dataset Overview & Data Quality | **#5** |
| **T1 Q1**: Peak month (VND + %) | **#6** |
| **T1 Q2**: High-spend provinces, low digital share | **#7** |
| **T1 Q3**: Top category by count vs. by spend + ticket size | **#8 left** |
| **T1 Q4**: Age cohort active but low health + spending metrics | **#8 right** |
| **T1**: Spending decomposition + business interpretation | **#9** |
| **T2**: Health score distribution | **#10** |
| **T2**: Main factors of low health | **#11 left** |
| **T2**: Differences by occupation, age, province | **#11 right** |
| **T2**: Stressed-but-engaged crossover segment (rule + profile) | **#12** |
| **T3**: Engagement distribution + segment share | **#13 left** |
| **T3**: Channel adoption breakdown (5 channels) | **#13 right** |
| **T3**: Category diversity ↔ engagement | **#14 top** |
| **T3**: Recency & frequency ↔ engagement | **#14 top** |
| **T3**: Healthy-but-disengaged segment + cutoff justification | **#14 bottom** |
| **T4**: Preprocessed dataset + feature engineering | **#15** |
| **T4**: Segmentation model + validation | **#16** |
| **T4**: Segment profiles + differentiators | **#17** |
| **T4**: Post-segmentation comparison + limitations + future work | **#18** |
| **T5**: 6 non-punitive interventions (target + data + reach) | **#19** |
| **T5**: Prioritisation + credit-decision rule + ethical statement | **#20** |
| Key Takeaways | **#21** |
| Thank You & Contact | **#22** |
