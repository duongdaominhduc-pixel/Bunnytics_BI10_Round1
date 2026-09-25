"""
Preprocessing Module
Data cleaning, transformation, and feature engineering utilities.
"""
import pandas as pd
import numpy as np


def check_missing(df, name="dataset"):
    """Report missing values for a dataframe."""
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    report = pd.DataFrame({
        'missing_count': missing,
        'missing_pct': missing_pct
    }).query('missing_count > 0').sort_values('missing_pct', ascending=False)
    print(f"\n--- Missing Values Report: {name} ---")
    if report.empty:
        print("No missing values found.")
    else:
        print(report)
    return report


def check_duplicates(df, subset, name="dataset"):
    """Check for duplicate rows based on a subset of columns."""
    dupes = df.duplicated(subset=subset).sum()
    print(f"[{name}] Duplicates on {subset}: {dupes}")
    return dupes


def create_age_cohorts(df, age_col='age'):
    """Bin age into cohorts."""
    bins = [0, 25, 35, 45, 55, 100]
    labels = ['18-25', '26-35', '36-45', '46-55', '56+']
    df['age_cohort'] = pd.cut(df[age_col], bins=bins, labels=labels, right=True)
    return df
