"""
Script to download stroke prediction datasets from multiple sources
"""
import os
import requests
import pandas as pd
from datasets import load_dataset

# Paths
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw")

def download_kaggle_dataset():
    """
    Download Stroke Prediction Dataset from Kaggle (via direct URL)
    Source: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
    License: CC0 Public Domain
    """
    print("=" * 50)
    print("Downloading Kaggle Stroke Prediction Dataset...")
    print("=" * 50)
    
    # Direct download URL (healthcare-dataset-stroke-data.csv)
    url = "https://raw.githubusercontent.com/fedesoriano/stroke-prediction-dataset/main/healthcare-dataset-stroke-data.csv"
    
    try:
        df = pd.read_csv(url)
        output_path = os.path.join(RAW_DATA_DIR, "stroke_kaggle.csv")
        df.to_csv(output_path, index=False)
        print(f"✅ Downloaded: {output_path}")
        print(f"   - Rows: {len(df)}")
        print(f"   - Columns: {df.columns.tolist()}")
        print(f"   - Source: Kaggle (fedesoriano)")
        print(f"   - License: CC0 Public Domain")
        return df
    except Exception as e:
        print(f"❌ Error downloading from GitHub: {e}")
        print("   Trying alternative method...")
        return None

def download_huggingface_dataset():
    """
    Download Stroke Prediction Dataset from HuggingFace
    Source: https://huggingface.co/datasets/Nnaodeh/Stroke_Prediction_Dataset
    License: CC0
    """
    print("\n" + "=" * 50)
    print("Downloading HuggingFace Stroke Prediction Dataset...")
    print("=" * 50)
    
    try:
        dataset = load_dataset("Nnaodeh/Stroke_Prediction_Dataset", split="train")
        df = dataset.to_pandas()
        output_path = os.path.join(RAW_DATA_DIR, "stroke_huggingface.csv")
        df.to_csv(output_path, index=False)
        print(f"✅ Downloaded: {output_path}")
        print(f"   - Rows: {len(df)}")
        print(f"   - Columns: {df.columns.tolist()}")
        print(f"   - Source: HuggingFace (Nnaodeh)")
        print(f"   - License: CC0")
        return df
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def create_synthetic_dataset(base_df, n_samples=500):
    """
    Create a synthetic dataset with some variations
    This simulates having a third data source
    """
    print("\n" + "=" * 50)
    print("Creating Synthetic Dataset (simulated third source)...")
    print("=" * 50)
    
    if base_df is None:
        print("❌ No base dataset available")
        return None
    
    import numpy as np
    np.random.seed(42)
    
    # Sample and add noise
    df_synthetic = base_df.sample(n=min(n_samples, len(base_df)), replace=True).copy()
    
    # Add some noise to numeric columns
    if 'age' in df_synthetic.columns:
        df_synthetic['age'] = df_synthetic['age'] + np.random.normal(0, 2, len(df_synthetic))
        df_synthetic['age'] = df_synthetic['age'].clip(0, 100).astype(int)
    
    if 'avg_glucose_level' in df_synthetic.columns:
        df_synthetic['avg_glucose_level'] = df_synthetic['avg_glucose_level'] + np.random.normal(0, 10, len(df_synthetic))
        df_synthetic['avg_glucose_level'] = df_synthetic['avg_glucose_level'].clip(50, 300)
    
    if 'bmi' in df_synthetic.columns:
        # Add more missing values to simulate incomplete data
        missing_mask = np.random.random(len(df_synthetic)) < 0.15
        df_synthetic.loc[missing_mask, 'bmi'] = np.nan
    
    # Reset index
    df_synthetic = df_synthetic.reset_index(drop=True)
    df_synthetic['id'] = range(100000, 100000 + len(df_synthetic))
    
    output_path = os.path.join(RAW_DATA_DIR, "stroke_synthetic.csv")
    df_synthetic.to_csv(output_path, index=False)
    print(f"✅ Created: {output_path}")
    print(f"   - Rows: {len(df_synthetic)}")
    print(f"   - Columns: {df_synthetic.columns.tolist()}")
    print(f"   - Source: Synthetic (generated from base data)")
    print(f"   - License: N/A (synthetic)")
    return df_synthetic

def create_data_info():
    """Create a JSON file with dataset information"""
    import json
    
    data_info = {
        "datasets": [
            {
                "filename": "stroke_kaggle.csv",
                "source": "Kaggle",
                "url": "https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset",
                "license": "CC0 Public Domain",
                "description": "Stroke Prediction Dataset - used to predict whether a patient is likely to get stroke based on input parameters",
                "columns": ["id", "gender", "age", "hypertension", "heart_disease", "ever_married", 
                           "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status", "stroke"]
            },
            {
                "filename": "stroke_huggingface.csv",
                "source": "HuggingFace",
                "url": "https://huggingface.co/datasets/Nnaodeh/Stroke_Prediction_Dataset",
                "license": "CC0",
                "description": "Stroke Prediction Dataset from HuggingFace Datasets Hub",
                "columns": ["id", "gender", "age", "hypertension", "heart_disease", "ever_married", 
                           "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status", "stroke"]
            },
            {
                "filename": "stroke_synthetic.csv",
                "source": "Synthetic",
                "url": "N/A",
                "license": "N/A",
                "description": "Synthetic dataset generated from base data for data fusion demonstration",
                "columns": ["id", "gender", "age", "hypertension", "heart_disease", "ever_married", 
                           "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status", "stroke"]
            }
        ]
    }
    
    output_path = os.path.join(RAW_DATA_DIR, "data_info.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data_info, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Created data info: {output_path}")

def main():
    print("\n" + "=" * 60)
    print("   STROKE PREDICTION DATA COLLECTION")
    print("=" * 60)
    
    # Create directory if not exists
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    
    # Download datasets
    df_kaggle = download_kaggle_dataset()
    df_hf = download_huggingface_dataset()
    
    # Create synthetic dataset
    base_df = df_kaggle if df_kaggle is not None else df_hf
    create_synthetic_dataset(base_df, n_samples=500)
    
    # Create data info file
    create_data_info()
    
    print("\n" + "=" * 60)
    print("   DATA COLLECTION COMPLETE!")
    print("=" * 60)
    print(f"\n📁 Data saved to: {RAW_DATA_DIR}")

if __name__ == "__main__":
    main()
