"""
Utility functions for Stroke Prediction Project
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.metrics import (
    roc_auc_score, average_precision_score, f1_score,
    recall_score, precision_score, confusion_matrix,
    roc_curve, precision_recall_curve
)

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
FIGURES_DIR = PROJECT_ROOT / 'results' / 'figures'
MODELS_DIR = PROJECT_ROOT / 'results' / 'models'


def load_raw_data():
    """Load all raw datasets"""
    datasets = {}
    for file in RAW_DATA_DIR.glob('*.csv'):
        name = file.stem
        datasets[name] = pd.read_csv(file)
    return datasets


def load_processed_data(pipeline='M1'):
    """Load processed data for a specific missing pipeline"""
    return pd.read_csv(PROCESSED_DATA_DIR / f'stroke_{pipeline}.csv')


def plot_missing_analysis(df, figsize=(12, 5)):
    """
    Plot missing data analysis
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    figsize : tuple
        Figure size
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    # Missing percentage
    missing_pct = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)
    missing_pct = missing_pct[missing_pct > 0]
    
    if len(missing_pct) > 0:
        axes[0].barh(missing_pct.index, missing_pct.values, color='coral')
        axes[0].set_xlabel('Missing %')
        axes[0].set_title('Missing Data by Column')
    else:
        axes[0].text(0.5, 0.5, 'No missing data', ha='center', va='center')
        axes[0].set_title('Missing Data by Column')
    
    # Missing matrix
    import missingno as msno
    msno.matrix(df, ax=axes[1], sparkline=False)
    axes[1].set_title('Missing Data Matrix')
    
    plt.tight_layout()
    return fig


def plot_target_distribution(y, figsize=(10, 4)):
    """
    Plot target variable distribution
    
    Parameters:
    -----------
    y : array-like
        Target variable
    figsize : tuple
        Figure size
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    # Count
    unique, counts = np.unique(y, return_counts=True)
    colors = ['#2ecc71', '#e74c3c']
    
    axes[0].bar(['No Stroke', 'Stroke'], counts, color=colors)
    axes[0].set_title('Stroke Distribution (Count)')
    axes[0].set_ylabel('Count')
    
    # Percentage
    axes[1].pie(counts, labels=['No Stroke', 'Stroke'], autopct='%1.1f%%',
                colors=colors, explode=[0, 0.1])
    axes[1].set_title('Stroke Distribution (%)')
    
    plt.tight_layout()
    return fig


def plot_numeric_by_target(df, numeric_cols, target_col='stroke', figsize=(15, 5)):
    """
    Plot numeric variables distribution by target
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    numeric_cols : list
        List of numeric column names
    target_col : str
        Target column name
    figsize : tuple
        Figure size
    """
    n_cols = len(numeric_cols)
    fig, axes = plt.subplots(1, n_cols, figsize=figsize)
    
    if n_cols == 1:
        axes = [axes]
    
    for ax, col in zip(axes, numeric_cols):
        sns.violinplot(data=df, x=target_col, y=col, ax=ax, palette=['#2ecc71', '#e74c3c'])
        ax.set_title(f'{col} by Stroke Status')
        ax.set_xticklabels(['No Stroke', 'Stroke'])
    
    plt.tight_layout()
    return fig


def evaluate_classifier(y_true, y_pred, y_prob=None):
    """
    Evaluate classification model
    
    Parameters:
    -----------
    y_true : array-like
        True labels
    y_pred : array-like
        Predicted labels
    y_prob : array-like, optional
        Predicted probabilities
    
    Returns:
    --------
    dict : Dictionary of metrics
    """
    metrics = {
        'F1-Score': f1_score(y_true, y_pred),
        'Recall': recall_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, zero_division=0)
    }
    
    if y_prob is not None:
        metrics['ROC-AUC'] = roc_auc_score(y_true, y_prob)
        metrics['PR-AUC'] = average_precision_score(y_true, y_prob)
    
    return metrics


def plot_model_evaluation(y_true, y_pred, y_prob, model_name='Model', figsize=(15, 5)):
    """
    Plot ROC curve, PR curve, and confusion matrix
    
    Parameters:
    -----------
    y_true : array-like
        True labels
    y_pred : array-like
        Predicted labels
    y_prob : array-like
        Predicted probabilities
    model_name : str
        Model name for title
    figsize : tuple
        Figure size
    """
    fig, axes = plt.subplots(1, 3, figsize=figsize)
    
    # ROC Curve
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    roc_auc = roc_auc_score(y_true, y_prob)
    
    axes[0].plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC (AUC = {roc_auc:.3f})')
    axes[0].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    axes[0].set_xlabel('False Positive Rate')
    axes[0].set_ylabel('True Positive Rate')
    axes[0].set_title(f'ROC Curve - {model_name}')
    axes[0].legend(loc='lower right')
    
    # PR Curve
    precision, recall, _ = precision_recall_curve(y_true, y_prob)
    pr_auc = average_precision_score(y_true, y_prob)
    
    axes[1].plot(recall, precision, color='green', lw=2, label=f'PR (AUC = {pr_auc:.3f})')
    axes[1].axhline(y=y_true.mean(), color='navy', linestyle='--')
    axes[1].set_xlabel('Recall')
    axes[1].set_ylabel('Precision')
    axes[1].set_title(f'PR Curve - {model_name}')
    axes[1].legend(loc='upper right')
    
    # Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[2],
                xticklabels=['No Stroke', 'Stroke'],
                yticklabels=['No Stroke', 'Stroke'])
    axes[2].set_xlabel('Predicted')
    axes[2].set_ylabel('Actual')
    axes[2].set_title(f'Confusion Matrix - {model_name}')
    
    plt.tight_layout()
    return fig


def plot_feature_importance(feature_names, importances, top_n=10, figsize=(10, 6)):
    """
    Plot feature importance
    
    Parameters:
    -----------
    feature_names : list
        List of feature names
    importances : array-like
        Feature importances
    top_n : int
        Number of top features to show
    figsize : tuple
        Figure size
    """
    # Create dataframe and sort
    fi_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values('Importance', ascending=False).head(top_n)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    colors = plt.cm.RdYlGn(np.linspace(0.2, 0.8, len(fi_df)))
    ax.barh(fi_df['Feature'], fi_df['Importance'], color=colors[::-1])
    ax.set_xlabel('Importance')
    ax.set_title('Feature Importance')
    ax.invert_yaxis()
    
    plt.tight_layout()
    return fig


def print_metrics_table(results_df, sort_by='ROC-AUC'):
    """
    Print a formatted metrics table
    
    Parameters:
    -----------
    results_df : pd.DataFrame
        Results dataframe
    sort_by : str
        Column to sort by
    """
    sorted_df = results_df.sort_values(sort_by, ascending=False)
    
    print("\n" + "="*80)
    print(f"{'Pipeline':<12} {'Model':<22} {'ROC-AUC':<10} {'PR-AUC':<10} {'F1':<10} {'Recall':<10}")
    print("="*80)
    
    for _, row in sorted_df.iterrows():
        print(f"{row['Pipeline']:<12} {row['Model']:<22} {row['ROC-AUC']:<10.4f} {row['PR-AUC']:<10.4f} {row['F1-Score']:<10.4f} {row['Recall']:<10.4f}")


if __name__ == "__main__":
    print("Utility functions loaded successfully!")
    print(f"Project root: {PROJECT_ROOT}")
