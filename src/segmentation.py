"""
Segmentation Module
Customer segmentation utilities (rule-based and clustering).
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def aggregate_to_consumer_level(df_health):
    """Aggregate consumer-month data to consumer-level (mean across months)."""
    numeric_cols = df_health.select_dtypes(include=[np.number]).columns.tolist()
    exclude = ['consumer_id']
    numeric_cols = [c for c in numeric_cols if c not in exclude]

    agg = df_health.groupby('consumer_id')[numeric_cols].mean().reset_index()

    # Add demographic info (take first occurrence)
    demo_cols = ['age', 'gender', 'occupation', 'province_city']
    demo = df_health.groupby('consumer_id')[demo_cols].first().reset_index()
    agg = agg.merge(demo, on='consumer_id', how='left', suffixes=('', '_demo'))

    return agg


def rule_based_segments(df, health_col='financial_health_score', 
                        engagement_col='engagement_score',
                        online_col='online_spend_ratio',
                        essential_col='essential_spend_ratio'):
    """Assign customers to 6 segments using rule-based logic."""
    conditions = [
        (df[health_col] >= 60) & (df[engagement_col] >= 60),
        (df[health_col] >= 60) & (df[engagement_col] < 40),
        (df[health_col] < 40) & (df[engagement_col] >= 60),
        (df[health_col] < 40) & (df[engagement_col] < 40),
        (df[online_col] >= df[online_col].quantile(0.75)),
        (df[essential_col] >= df[essential_col].quantile(0.75)),
    ]
    labels = [
        'Healthy & Highly Engaged',
        'Healthy but Disengaged',
        'Stretched but Engaged',
        'Vulnerable & Disengaged',
        'Emerging Digital',
        'Essential-Focused',
    ]
    # Apply in order; first match wins
    df['segment'] = 'Other'
    for cond, label in zip(reversed(conditions), reversed(labels)):
        df.loc[cond, 'segment'] = label
    return df
