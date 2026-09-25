# 📋 Bunnytics — Task Assignment Board
## BI10 Round 01 · Nhóm 3 người

> **Repo**: [Bunnytics_BI10_Round1](https://github.com/duongdaominhduc-pixel/Bunnytics_BI10_Round1)
> **Deadline**: 23:59, September 28, 2026
> **Last updated**: 2026-09-25

---

## 👥 Team Members

| Ký hiệu | Tên | Role | GitHub |
|----------|-----|------|--------|
| **A** | _[Tên thành viên 1]_ | Leader / Data Analyst | _@username_ |
| **B** | _[Tên thành viên 2]_ | Data Analyst | _@username_ |
| **C** | _[Tên thành viên 3]_ | Data Analyst / Designer | _@username_ |

---

## 🚦 Legend

- 🔴 Not started · 🟡 In progress · 🟢 Done
- **Primary**: Người chịu trách nhiệm chính — làm code + viết manuscript
- **Support**: Người review, ghép slide, hoặc hỗ trợ khi cần

---

## ⚙️ Phase 0–1: Setup & Data Quality

| # | Task | Primary | Support | Status | Notes |
|---|------|---------|---------|--------|-------|
| 0.1 | Setup môi trường, venv, install requirements | A | — | 🟢 | Xong |
| 0.2 | Load data, kiểm tra cột/schema | A | — | 🟢 | Xong — 10,992 rows (sẽ giải thích) |
| 1.1 | Missing values analysis | A | — | 🟢 | next_month_low_health_flag: 999 nulls (Dec) |
| 1.2 | Duplicate detection (consumer_id × month) | A | — | 🟢 | 0 dupes |
| 1.3 | Outlier detection (scores, VND) | A | — | 🟢 | no neg spend |
| 1.4 | Consistency check: ratio fields sum đúng không? | A | — | 🔴 | |
| 1.5 | Temporal coverage: tại sao 10,992 ≠ 999×12? | A | — | 🔴 | |
| 1.6 | Cross-dataset link: consumer_id match giữa 2 file | A | — | 🔴 | |

---

## 📊 Task 1: Exploratory Data Analysis (EDA) — 20%

> **Đề yêu cầu trả lời đúng 5 câu hỏi sau, kèm số liệu, tỷ lệ, biểu đồ.**

| # | Câu hỏi (nguyên văn đề) | Primary | Support | Status |
|---|------------------------|---------|---------|--------|
| **Q1** | _Which month records the highest total spend, and how much does it account for (in VND and as a % of annual spend) compared to the lowest spending month? Is this peak driven primarily by higher transaction count or larger ticket sizes? What does this pattern reveal about consumer spending behavior during peak periods?_ | B | — | 🔴 |
| **Q2** | _Compare the proportion of Essential vs. Discretionary spend between financially stressed customers (financial_health_score < 40) and healthy customers (financial_health_score ≥ 80). Based on the data, what does this spending composition reveal about how financial stress alters a customer's budget allocation?_ | B | — | 🔴 |
| **Q3** | _Identify 2 or more provinces/cities that generate high total spend volume but have a lower-than-average digital transaction share. Compare their channel breakdown (POS vs. digital channels) to quantify and explain the nature of their digital adoption gap._ | B | — | 🔴 |
| **Q4** | _Identify the top category by transaction count and the top category by total spend volume. Compare their average ticket sizes (VND per transaction) and explain how consumer usage behavior differs between these two categories._ | B | — | 🔴 |
| **Q5** | _Which age cohort maintains active transaction frequency while recording the lowest average financial_health_score? Contrast their spending metrics (essential spend ratio and spend-to-income ratio) with other age cohorts to explain the drivers of their financial vulnerability._ | B | A | 🔴 |

**Deliverables (đề yêu cầu):**
- Quantitative answers to Q1–Q5 với số chính xác, %, ratio
- Decomposition: transaction volume vs. ticket size; essential vs. discretionary
- Nhận xét business về consumer behavior
- Biểu đồ phù hợp từng phần

> 📝 Sau khi xong → viết kết quả vào `manuscript/task1_eda_manuscript.md`

---

## 💊 Task 2: Financial Health Analysis — 20%

> **Đề yêu cầu phân tích health score và tìm crossover segment.**
> **Lưu ý đề**: Dùng ratio-based fields, KHÔNG dùng raw VND để so sánh. Mọi claim phải có số hoặc biểu đồ.

| # | Deliverable (nguyên văn đề) | Primary | Support | Status |
|---|--------------------------|---------|---------|--------|
| **2.1** | _Distribution of financial_health_score_ — phân phối score, trend theo tháng, breakdown theo segment | A | — | 🔴 |
| **2.2** | _Main factors associated with low health_ — các biến tương quan mạnh với score thấp (dùng ratio features) | A | — | 🔴 |
| **2.3** | _Differences by occupation, age, and province_ — health score khác nhau như thế nào theo nhân khẩu học | A | C | 🔴 |
| **2.4** | _Identify customers who are financially stressed but highly engaged; define and apply a clear, reproducible rule to identify this crossover segment_ — đưa ra rule (ví dụ: health_score < 40 & engagement_score ≥ X), giải thích lý do chọn ngưỡng, số lượng và profile nhóm này | A | B | 🔴 |

**Nguồn data chính**: `consumer_financial_health_engagement_2025.csv`
**Nguồn phụ (nếu cần chi tiết)**: `consumer_transactions_2025.csv` (merchant/category/timestamp)

> 📝 Sau khi xong → viết kết quả vào `manuscript/task2_health_manuscript.md`

---

## 📱 Task 3: Customer Engagement Analysis — 20%

> **Đề yêu cầu 6 objectives, deliverables tương ứng.**

| # | Objective (nguyên văn đề) | Deliverable | Primary | Support | Status |
|---|--------------------------|-------------|---------|---------|--------|
| **3.1** | _Show how engagement_score is spread across the customer base_ | Distribution + share of customers in each engagement segment | B | — | 🔴 |
| **3.2** | _Show which channels customers use, and how much of their spend is digital_ | Channel adoption breakdown (POS, QR, E-commerce, Mobile App, Recurring) + avg online spend share | B | — | 🔴 |
| **3.3** | _Show how many spending categories a customer typically uses_ | Category diversity range + mối liên hệ với engagement score | B | — | 🔴 |
| **3.4** | _Show how often and how recently customers transact_ | Recency & frequency ranges + link to engagement | B | — | 🔴 |
| **3.5** | _Find customers who are financially healthy but not engaged — a group at risk of leaving even though they are good customers. State the score cutoff used to define "high" and "low", since the task does not give one_ | Exact size & profile của nhóm high-health, low-engagement + giải thích tại sao chọn cutoff này (so với stricter/looser) | B | A | 🔴 |
| **3.6** | _Use a chart that fits the data for each part, so a reader can see the pattern, not just read numbers_ | Mỗi phần dùng chart type phù hợp | C | B | 🔴 |

> 📝 Sau khi xong → viết kết quả vào `manuscript/task3_engagement_manuscript.md`

---

## 🗂️ Task 4: Customer Segmentation — 20%

> **Đề yêu cầu xây dựng model phân khúc data-driven.**

### Bước 1: Data Preprocessing & Feature Engineering

| # | Task | Primary | Support | Status |
|---|------|---------|---------|--------|
| **4.1** | Chuẩn bị features từ 4 nhóm: Demographics (age, gender, occupation, province_city), Financial Health (income, credit limit, utilization, health score, avg transaction, volatility...), Engagement (transaction count, active days, engagement score...), Spending Behavior (category diversity, essential/discretionary/online ratio...) | A | B | 🔴 |

### Bước 2: Customer Segmentation Model

| # | Task | Primary | Support | Status |
|---|------|---------|---------|--------|
| **4.2** | Feature selection & engineering (chọn metrics key, tính thêm ratios nếu cần) | A | B | 🔴 |
| **4.3** | Model selection & setup: chọn K-Means, GMM, hoặc Rule-Based Matrix — **giải thích lý do chọn** | A | B | 🔴 |
| **4.4** | Implementation & validation: đảm bảo 100% coverage, validate cluster quality hoặc rule distribution | A | — | 🔴 |
| **4.5** | Customer profiling: gán business label cho từng segment (6 nhóm gợi ý, không bắt buộc): **Financially Healthy & Highly Engaged · Financially Healthy but Disengaged · Financially Stretched but Highly Engaged · Low Engagement & Financially Vulnerable · Emerging Digital Customers · Essential-Spend-Focused Customers** | A | B | 🔴 |
| **4.6** | Post-segmentation analysis: so sánh các nhóm side-by-side, nêu key behavioral differences | A | B | 🔴 |

### Bước 3: Limitations & Future Work

| # | Task | Primary | Support | Status |
|---|------|---------|---------|--------|
| **4.7** | Xác định hạn chế kỹ thuật & operational của model | A | B | 🔴 |
| **4.8** | Gợi ý cải thiện cho future work | A | — | 🔴 |

**Deliverables (đề yêu cầu):**
- Preprocessed dataset với tất cả engineered features
- Segmentation model (clustering OR rule-based) + segment profiles
- Limitations & Future Work

> 📝 Sau khi xong → viết kết quả vào `manuscript/task4_segmentation_manuscript.md`

---

## 💡 Task 5: Business Recommendations — 15%

> **Đề yêu cầu 6 loại intervention, mỗi cái phải link với số liệu thực từ data.**
> **Constraint tuyệt đối**: KHÔNG đề xuất từ chối tín dụng dựa trên financial_health_score.

| # | Tool Type | Yêu cầu cụ thể | Primary | Support | Status |
|---|-----------|---------------|---------|---------|--------|
| **5.1** | Budgeting Tools | Link với finding thực từ data, có target group + số lượng KH reach được | C | A | 🔴 |
| **5.2** | Spend Alerts | Link với finding thực từ data, có target group + số lượng KH reach được | C | A | 🔴 |
| **5.3** | Financial-Planning Reminders | Link với finding thực từ data, có target group + số lượng KH reach được | C | B | 🔴 |
| **5.4** | Financial-Education Content | Link với finding thực từ data, có target group + số lượng KH reach được | C | B | 🔴 |
| **5.5** | Digital-Channel Nudges | Link với finding thực từ data, có target group + số lượng KH reach được | C | B | 🔴 |
| **5.6** | Suitable Product Suggestions | Link với finding thực từ data, có target group + số lượng KH reach được | C | A | 🔴 |
| **5.7** | Prioritisation: rank 6 ideas by **reach** và **driver strength** | Bảng ranking rõ ràng | C | A | 🔴 |
| **5.8** | Credit-decision rule statement: _"financial_health_score must never be used to deny credit, cut a credit limit, or block an account"_ | Statement explicit trên slide | C | — | 🔴 |

**Deliverables (đề yêu cầu):**
- 1 clear proposal cho mỗi trong 6 tool types, mỗi cái linked to a real number/column from data
- Clear target groups với exact sizes và percentages
- A clear statement of the credit-decision rule

> 📝 Sau khi xong → viết kết quả vào `manuscript/task5_recommendations_manuscript.md`

---

## 🖼️ Slide Proposal (max 22 slides)

| # | Slide | Người làm | Dựa trên | Status |
|---|-------|----------|----------|--------|
| S1 | Cover | C | — | 🔴 |
| S2 | Executive Summary | A | Tất cả manuscripts (viết sau cùng) | 🔴 |
| S3 | Table of Contents | C | — | 🔴 |
| S4–5 | Introduction to Case (business context + data quality) | C | A | 🔴 |
| S6–9 | Task 1 — EDA (4 slides) | C | `task1_eda_manuscript.md` | 🔴 |
| S10–12 | Task 2 — Financial Health (3 slides) | C | `task2_health_manuscript.md` | 🔴 |
| S13–14 | Task 3 — Engagement (2 slides) | C | `task3_engagement_manuscript.md` | 🔴 |
| S15–18 | Task 4 — Segmentation (4 slides) | C | `task4_segmentation_manuscript.md` | 🔴 |
| S19–20 | Task 5 — Recommendations (2 slides) | C | `task5_recommendations_manuscript.md` | 🔴 |
| S21 | Key Takeaways | A | — | 🔴 |
| S22 | Thank You / Contact | C | — | 🔴 |

**File name**: `Bunnytics_[LeaderName]_BI10_R01.pptx`
**Format**: 16:9, max 100 MB, ngôn ngữ: **English**

---

## 📈 Overall Progress

| Task | Người phụ trách | Weight | Status | % |
|------|----------------|--------|--------|---|
| Phase 0–1: Setup & DQ | A | — | 🟡 | 30% |
| Task 1: EDA | B | 20% | 🔴 | 0% |
| Task 2: Financial Health | A | 20% | 🔴 | 0% |
| Task 3: Engagement | B | 20% | 🔴 | 0% |
| Task 4: Segmentation | A | 20% | 🔴 | 0% |
| Task 5: Recommendations | C | 15% | 🔴 | 0% |
| Communication/Slide | C | 5% | 🔴 | 0% |
| **Total** | | **100%** | 🟡 | **~5%** |

---

## 📌 Git Workflow

<<<<<<< HEAD
1. **Branch naming**: `feature/task1-eda`, `feature/task2-health`, `feature/task4-segmentation`, ...
2. **Commit messages**: `[Task X] Brief description` — ví dụ `[Task 1] Add Q1 monthly spend analysis`
3. **Pull requests**: Tạo PR khi xong mỗi task, assign reviewer = 1 người khác trong nhóm
4. **Data files**: KHÔNG commit file CSV lớn (đã có `.gitignore`). Mỗi người tự download dataset vào folder `ĐỀ BÀI/DATASET/`
5. **Communication**: Cập nhật status trong file này khi bắt đầu (🟡) và hoàn thành (🟢) task

---

## ✅ Progress Tracker

| Phase | Task | Status | % Complete |
|-------|------|--------|------------|
| Phase 0–1 | Setup & Data Quality | 🟢 | 100% |
| Phase 2 | Task 1 — EDA | 🔴 | 0% |
| Phase 3 | Task 2 — Financial Health | 🔴 | 0% |
| Phase 4 | Task 3 — Engagement | 🔴 | 0% |
| Phase 5 | Task 4 — Segmentation | 🔴 | 0% |
| Phase 6 | Task 5 — Recommendations | 🔴 | 0% |
| Slides | Proposal (22 slides) | 🔴 | 0% |
| **Overall** | | 🟡 | **~5%** |
=======
1. **Branches**: `feature/task1-eda` · `feature/task2-health` · `feature/task3-engagement` · `feature/task4-segmentation` · `feature/task5-recs`
2. **Commit format**: `[Task X] Mô tả ngắn gọn` — ví dụ: `[Task 1] Q1 monthly spend analysis with chart`
3. **Manuscript first**: Xong notebook → điền `manuscript/task_X_...md` → PR → C làm slide
4. **Không commit CSV lớn** — tự copy vào `ĐỀ BÀI/DATASET/` local
>>>>>>> 69eb1e7 (Rewrite task assignment board with exact questions from BI10_ROUND01.pdf)
