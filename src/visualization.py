"""
Visualization Module
Reusable plotting functions with consistent styling.
"""
import matplotlib.pyplot as plt
import seaborn as sns

# BI10 Color Palette
COLORS = {
    'primary': '#1E3A5F',
    'accent1': '#00B4D8',
    'accent2': '#FF6B35',
    'positive': '#06D6A0',
    'negative': '#EF476F',
    'neutral': '#8B95A5',
    'bg': '#F8F9FA',
    'text': '#212529',
}

SEGMENT_COLORS = {
    'Healthy & Engaged': COLORS['positive'],
    'Healthy but Disengaged': COLORS['accent1'],
    'Stretched but Engaged': COLORS['accent2'],
    'Vulnerable & Disengaged': COLORS['negative'],
    'Emerging Digital': '#8B5CF6',
    'Essential-Focused': COLORS['neutral'],
}


def set_style():
    """Apply consistent plot styling."""
    sns.set_theme(style='whitegrid', font_scale=1.1)
    plt.rcParams.update({
        'figure.figsize': (12, 6),
        'figure.dpi': 150,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'font.family': 'sans-serif',
    })


def save_fig(fig, name, dpi=200):
    """Save figure to outputs/figures/."""
    from pathlib import Path
    out_dir = Path(__file__).parent.parent / "outputs" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / f"{name}.png", dpi=dpi, bbox_inches='tight')
    print(f"Saved: outputs/figures/{name}.png")
