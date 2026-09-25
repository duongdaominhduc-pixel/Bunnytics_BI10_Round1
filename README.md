# Bunnytics — BI10 Round 01
## Consumer Financial Health & Engagement

> Understanding Spending Behaviour and Building Meaningful Customer Segments

### 📋 Project Structure

```
├── ĐỀ BÀI/                    # Problem statement & datasets (read-only)
│   ├── BI10_ROUND01.pdf
│   └── DATASET/
├── notebooks/                   # Jupyter analysis notebooks
│   ├── 00_data_quality.ipynb
│   ├── 01_eda.ipynb
│   ├── 02_financial_health.ipynb
│   ├── 03_engagement.ipynb
│   ├── 04_segmentation.ipynb
│   └── 05_recommendations.ipynb
├── src/                         # Reusable Python modules
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── visualization.py
│   └── segmentation.py
├── outputs/                     # Analysis outputs
│   ├── figures/
│   ├── tables/
│   └── report/
├── BI10_project_plan.md         # Detailed project plan (6 phases)
├── BI10_slide_outline.md        # Slide proposal outline (22 slides)
├── requirements.txt
└── README.md
```

### 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/duongdaominhduc-pixel/Bunnytics_BI10_Round1.git
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 📊 Datasets

| File | Grain | Rows | Cols |
|------|-------|------|------|
| `consumer_transactions_2025.csv` | 1 row/transaction | 1,852,394 | 28 |
| `consumer_financial_health_engagement_2025.csv` | 1 row/consumer/month | 10,992 | 30 |

> ⚠️ All data is **synthetic**. Use **ratios** for cross-customer comparison, not absolute VND values.

### 📝 Tasks

| Task | Description | Weight |
|------|-------------|--------|
| 1 | Exploratory Data Analysis | 20% |
| 2 | Financial Health Analysis | 20% |
| 3 | Customer Engagement Analysis | 20% |
| 4 | Customer Segmentation | 20% |
| 5 | Business Recommendations | 15% |

### 👥 Team

- **Team Name**: Bunnytics
- **Members**: [Update here]
