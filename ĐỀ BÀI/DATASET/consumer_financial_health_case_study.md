# Consumer Financial Health & Engagement: Understanding Spending Behaviour and Building Meaningful Customer Segments

*Synthetic teaching case study — Vietnam, 2025. All data is fabricated; no real individuals are represented.*

---

## Tóm tắt (Vietnamese summary)

Một công ty tài chính tiêu dùng tại Việt Nam muốn hiểu rõ **sức khỏe tài chính**, **mức độ tương tác** và **thói quen chi tiêu** của khách hàng dựa trên dữ liệu giao dịch giả lập năm 2025 (1.852.394 giao dịch, 999 khách hàng, 34 tỉnh/thành). Mục tiêu là xây dựng các **phân khúc khách hàng** có ý nghĩa và đề xuất **giải pháp hỗ trợ không mang tính trừng phạt** (công cụ quản lý ngân sách, cảnh báo chi tiêu, giáo dục tài chính, khuyến khích kênh số). Đây **không phải** bài toán chấm điểm tín dụng; `financial_health_score` tuyệt đối không được dùng để phê duyệt hay từ chối tín dụng. Dữ liệu là **giả lập**: danh tính, địa lý, cửa hàng, thu nhập và số dư đều được tạo tổng hợp và chỉ có ý nghĩa tương đối.

---

## 1. Business background

A Vietnamese consumer-finance company issues cards and short-term credit to retail
customers. Leadership wants to move from a reactive, collections-oriented view of
customers toward a **proactive financial-wellbeing** view: understanding how customers
spend, how healthy their finances look month to month, and how engaged they are with
the company's digital channels. The analytics team has assembled a synthetic
transaction dataset for 2025 to prototype this capability before touching production data.

## 2. Business problem

The company needs to answer:

- How healthy are customers financially, and which factors drive low health?
- How engaged are customers with transaction channels, and who is drifting?
- Where do spending habits differ by region, age, and occupation?
- Which customers are **financially healthy but disengaged** (retention/growth opportunity)?
- Which are **highly engaged but financially stretched** (support opportunity, not punishment)?
- How can the company group customers into **actionable segments** and design
  **non-punitive interventions**?

## 3. Dataset description

Two linked datasets are provided (random seed = 42):

| File | Grain | Rows | Columns |
|---|---|---|---|
| `consumer_transactions_2025` (parquet / csv.gz) | one row per transaction | 1,852,394 | 28 |
| `consumer_financial_health_engagement_2025.csv` | one row per consumer per month | 10,992 | 30 |

Coverage: **999 consumers**, **693 merchants**, **34 provinces/cities**, all of
calendar **2025**. Currency is VND (1 source unit = 25,000 VND). The data is re-themed from a
publicly available *simulated* card-transaction dataset; the original context has been
fully removed and identities/geography/merchants re-generated for Vietnam.

## 4. Unit of analysis

- **Transaction level** — behavioural detail (channel, category, amount, time).
- **Consumer-month level** — the primary analytical grain for health, engagement, and
  segmentation. One row summarises a customer's behaviour within a calendar month.

## 5. Data dictionary summary

Full definitions are in `data_dictionary_bilingual.xlsx`. Key fields:

- Identity & geography: `consumer_id`, `customer_name`, `gender`, `age`, `occupation`,
  `ward_commune`, `province_city`, `administrative_code`, coordinates, `local_population`.
- Spending: `spend_amount_vnd`, `spending_category`, `essential_spending_flag`,
  `transaction_channel`, `payment_method`, `online_transaction_flag`.
- Monthly aggregates & ratios: `total_spend_vnd`, `essential/discretionary/online_spend_vnd`,
  `transaction_count`, `active_transaction_days`, `category_diversity`,
  `essential_spend_ratio`, `online_spend_ratio`, `spend_to_income_ratio`,
  `credit_utilization_ratio`, `transaction_recency_days`, `spending_volatility`.
- Synthetic financials: `monthly_income_vnd`, `credit_limit_vnd`,
  `opening_balance_vnd`, `ending_balance_vnd` (**synthetic — not real values**).
- Scores & segments: `financial_health_score`, `financial_health_segment`,
  `engagement_score`, `engagement_segment`.
- Analytical target (optional): `next_month_low_health_flag`.

## 6. Learning objectives

By completing this case, learners will be able to:

1. Assess data quality and customer-level consistency in a transactional dataset.
2. Perform exploratory analysis of spending across time, category, region, and demographics.
3. Construct and interpret ratio-based financial-health and engagement indicators.
4. Build and defend customer segments (rule-based and/or clustering).
5. Translate analytical findings into **ethical, non-punitive** business actions.
6. (Advanced) Frame a leak-free, chronological classification problem and evaluate it
   with appropriate metrics.

## 7. Data quality considerations

- All timestamps fall inside 2025; `transaction_id` is unique; each `consumer_id` maps to
  a single name, birth date, and home address; each `merchant_id` maps to a single name.
- `spend_amount_vnd` is non-negative and rounded to 1,000 VND.
- **Synthetic financial fields** (income, credit limit, balances) are calibrated to each
  consumer's spending volume; their **absolute magnitudes are unrealistically high**
  relative to typical Vietnamese salaries because the underlying simulation is very
  transaction-dense. Treat the **ratios**, not the absolute VND figures, as meaningful.
- Ward/commune names are **illustrative**, not the official post-2025 list.
- All 25 mandatory quality checks pass (see `data_quality_report.md`).

## 8. Required analytical tasks

**Task 1 — Data quality assessment.** Missing values, duplicate transactions, outliers,
data consistency, customer-level consistency, temporal coverage.

**Task 2 — Exploratory data analysis.** Spending trends by month; spending by category,
province, and channel (online vs offline); age and occupation patterns; essential vs
discretionary spending.

**Task 3 — Financial health analysis.** Distribution of `financial_health_score`; the
main factors associated with low health; differences by occupation, age, and province;
identification of **financially stressed but highly engaged** customers.

**Task 4 — Customer engagement analysis.** Engagement distribution; channel adoption;
category diversity; recency and frequency; **high-health but low-engagement** customers.

**Task 5 — Customer segmentation.** Rule-based and/or clustering (e.g., k-means on scaled
ratio features, or a 2×2 health×engagement matrix). Suggested groups (not mandatory):

- Financially Healthy & Highly Engaged
- Financially Healthy but Disengaged
- Financially Stretched but Highly Engaged
- Low Engagement & Financially Vulnerable
- Emerging Digital Customers
- Essential-Spend-Focused Customers

**Task 6 — Business recommendations.** Propose **non-punitive** interventions: budgeting
tools, spend alerts, financial-planning reminders, financial-education content, digital-
channel nudges, and suitable product suggestions. **Do not** propose denying credit based
on `financial_health_score`.

## 9. Expected deliverables

A reproducible notebook or report containing: cleaned data + quality summary; EDA with
clear visuals; health and engagement analysis; a defended segmentation with profiles;
and a prioritised, ethical recommendation set. Optionally, a calibrated predictive model
for `next_month_low_health_flag`.

## 10. Evaluation rubric

| Criterion | Weight | What good looks like |
|---|---|---|
| Data quality & rigour | 15% | Consistency checks, honest handling of synthetic caveats |
| EDA depth & clarity | 20% | Insightful, well-visualised, segmented views |
| Health & engagement analysis | 20% | Correct interpretation of ratios and drivers |
| Segmentation | 20% | Reproducible, well-profiled, business-relevant groups |
| Recommendations | 15% | Actionable, prioritised, and **ethical/non-punitive** |
| Communication | 10% | Clear narrative for a business audience |

## 11. Ethical considerations

`financial_health_score` is a **wellbeing indicator, not a credit score**, and must never
be used to approve or deny credit. Recommendations must be supportive rather than punitive.
Because the data is synthetic, no real customer is profiled; nonetheless, learners should
practise the same fairness and privacy discipline they would apply to production data
(e.g., check whether interventions would disadvantage particular regions, ages, or occupations).

## 12. Limitations of synthetic data

- Identities, merchants, geography, income, credit and balances are **fabricated**.
- The source simulation is transaction-dense, so per-customer volumes and synthetic
  income magnitudes are higher than in reality; **ratios are the reliable signal**.
- Engagement skews high because every card is very active; differentiation comes mainly
  from digital adoption and category diversity.
- Ward/commune names are illustrative; only the 34 province names are canonical.
- Folding two source years onto 2025 preserves month/day/time-of-day but increases
  monthly volume relative to a single real year.

---

### Optional advanced modelling task

Predict `next_month_low_health_flag` (1 if next month's `financial_health_score` < 40).
Use features from month *t* to predict the label for month *t+1*; **December 2025 has no
label**. Use a **chronological split** (e.g., train Jan–Aug, validate Sep–Oct, test Nov),
never a random split, and never leak future information. Evaluate with **ROC-AUC, PR-AUC,
Recall, Precision, F1, Brier score, a calibration curve, and a confusion matrix**. This
target is an **analytical construct**, not a real default or risk label.
