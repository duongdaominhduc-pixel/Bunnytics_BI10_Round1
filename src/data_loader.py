"""
Data Loader Module
Handles loading and initial processing of the BI10 datasets.
"""
import pandas as pd
from pathlib import Path


DATA_DIR = Path(__file__).parent.parent / "ĐỀ BÀI" / "DATASET"

def load_transactions(filepath=None):
    """Load the transaction-level dataset."""
    if filepath is None:
        filepath = DATA_DIR / "consumer_transactions_2025.csv"
    return pd.read_csv(filepath)

def load_health_engagement(filepath=None):
    """Load the consumer-month level dataset."""
    if filepath is None:
        filepath = DATA_DIR / "consumer_financial_health_engagement_2025.csv"
    return pd.read_csv(filepath)

def load_data_dictionary(filepath=None):
    """Load the data dictionary."""
    if filepath is None:
        filepath = DATA_DIR / "data_dictionary.xlsx"
    return pd.read_excel(filepath)
