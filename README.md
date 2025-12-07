# 🧠 Stroke Prediction - Data Governance & Visualization Project

> **Bài Tập Lớn** - Dự án phân tích và dự đoán nguy cơ đột quỵ (Stroke) sử dụng các kỹ thuật Data Governance, Machine Learning và Visualization.

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Mục Lục

1. [Giới Thiệu](#-giới-thiệu)
2. [Yêu Cầu Bài Tập](#-yêu-cầu-bài-tập)
3. [Cấu Trúc Dự Án](#-cấu-trúc-dự-án)
4. [Dữ Liệu](#-dữ-liệu)
5. [Phương Pháp](#-phương-pháp)
6. [Kết Quả](#-kết-quả)
7. [Hướng Dẫn Chạy](#-hướng-dẫn-chạy)
8. [Kết Luận](#-kết-luận)

---

## 🎯 Giới Thiệu

### Bối Cảnh
Đột quỵ (Stroke) là nguyên nhân gây tử vong hàng đầu thế giới, chiếm khoảng 11% tổng số ca tử vong toàn cầu (WHO). Dự án này xây dựng mô hình Machine Learning để dự đoán nguy cơ đột quỵ dựa trên các đặc điểm sức khỏe và lối sống.

### Mục Tiêu
- **Thu thập & Tích hợp dữ liệu** từ nhiều nguồn (Kaggle, HuggingFace)
- **Xử lý Missing Data** với 3 phương pháp khác nhau
- **Xử lý Class Imbalance** với 3 kỹ thuật khác nhau  
- **So sánh 27 pipelines** (3 × 3 × 3 models)
- **Visualization** chi tiết cho phân tích EDA và kết quả modeling

---

## 📝 Yêu Cầu Bài Tập

### ✅ Checklist Hoàn Thành

| STT | Yêu Cầu | Trạng Thái | Ghi Chú |
|-----|---------|------------|---------|
| 1 | Thu thập dữ liệu từ ≥2 nguồn | ✅ Hoàn thành | Kaggle, HuggingFace, Synthetic |
| 2 | Data Fusion (tích hợp dữ liệu) | ✅ Hoàn thành | 5,610 records sau merge |
| 3 | Xử lý Missing Data (≥2 phương pháp) | ✅ Hoàn thành | M0, M1, M2 (3 phương pháp) |
| 4 | Xử lý Imbalanced Data (≥2 phương pháp) | ✅ Hoàn thành | I0, I1, I2 (3 phương pháp) |
| 5 | EDA & Visualization | ✅ Hoàn thành | 17 biểu đồ |
| 6 | Training & Evaluation Models | ✅ Hoàn thành | 27 experiments |
| 7 | So sánh kết quả các pipelines | ✅ Hoàn thành | Metrics comparison |
| 8 | Lưu trữ models & results | ✅ Hoàn thành | .pkl, .csv, .json |

---

## 📂 Cấu Trúc Dự Án

```
Data-Governance-Visualization/
├── 📁 data/
│   ├── 📁 raw/                          # Dữ liệu gốc
│   │   ├── stroke_kaggle.csv            # 5,110 records từ Kaggle
│   │   ├── stroke_huggingface.csv       # Mirror từ HuggingFace
│   │   ├── stroke_synthetic.csv         # 500 records synthetic
│   │   └── data_info.json               # Metadata
│   │
│   └── 📁 processed/                    # Dữ liệu đã xử lý
│       ├── stroke_merged_clean.csv      # 5,610 records sau merge
│       ├── stroke_M0.csv                # Listwise deletion (5,317 records)
│       ├── stroke_M1.csv                # Mean/Median imputation (5,610 records)
│       ├── stroke_M2.csv                # KNN imputation (5,610 records)
│       ├── model_results.csv            # Kết quả 27 experiments
│       ├── eda_summary.json             # EDA statistics
│       └── label_encoders.json          # Encoding mappings
│
├── 📁 notebooks/                        # Jupyter Notebooks
│   ├── 01_data_collection.ipynb         # Thu thập dữ liệu
│   ├── 02_data_fusion_cleaning.ipynb    # Fusion & Missing data
│   ├── 03_eda_visualization.ipynb       # EDA & Charts
│   └── 04_modeling.ipynb                # Model training & evaluation
│
├── 📁 results/
│   ├── 📁 figures/                      # Biểu đồ (17 files)
│   │   ├── eda_*.png                    # EDA visualizations
│   │   ├── missing_*.png                # Missing data analysis
│   │   ├── model_*.png                  # Model comparisons
│   │   ├── feature_importance.png       # Feature importance
│   │   └── best_model_evaluation.png    # Best model ROC/PR curves
│   │
│   └── 📁 models/                       # Trained models
│       ├── best_model.pkl               # Best model (Gradient Boosting)
│       └── model_summary.json           # Summary & metrics
│
├── 📁 src/                              # Source code
│   ├── download_data.py                 # Data download utilities
│   └── utils.py                         # Helper functions
│
├── requirements.txt                     # Python dependencies
└── README.md                            # Documentation (file này)
```

---

## 📊 Dữ Liệu

### Nguồn Dữ Liệu

| Nguồn | Số Records | Mô Tả |
|-------|------------|-------|
| **Kaggle** | 5,110 | Stroke Prediction Dataset |
| **HuggingFace** | 5,110 | Mirror dataset |
| **Synthetic** | 500 | Generated data cho data fusion demo |
| **Merged** | **5,610** | Sau khi deduplicate |

### Các Biến (Features)

| Biến | Kiểu | Mô Tả | Missing |
|------|------|-------|---------|
| `id` | int | ID bệnh nhân | 0% |
| `gender` | cat | Male/Female/Other | 0% |
| `age` | float | Tuổi (0.08 - 82) | 0% |
| `hypertension` | int | Cao huyết áp (0/1) | 0% |
| `heart_disease` | int | Bệnh tim (0/1) | 0% |
| `ever_married` | cat | Đã kết hôn (Yes/No) | 0% |
| `work_type` | cat | Loại công việc | 0% |
| `Residence_type` | cat | Urban/Rural | 0% |
| `avg_glucose_level` | float | Đường huyết TB | 0% |
| `bmi` | float | Chỉ số BMI | **5.22%** |
| `smoking_status` | cat | Tình trạng hút thuốc | 0% |
| `stroke` | int | **Target** (0/1) | 0% |

### Class Imbalance

```
Stroke Distribution:
├── No Stroke (0): 5,338 (95.17%) ████████████████████████████████████████
└── Stroke (1):      271 (4.83%)  ██

Imbalance Ratio: 1:19.7 (Severely Imbalanced)
```

---

## 🔬 Phương Pháp

### 1. Missing Data Handling

| Method | Code | Kỹ Thuật | Records |
|--------|------|----------|---------|
| **M0** | Listwise Deletion | Xóa rows có missing | 5,317 |
| **M1** | Mean/Median Imputation | Điền median cho BMI | 5,610 |
| **M2** | KNN Imputation | K-Nearest Neighbors (k=5) | 5,610 |

### 2. Imbalance Handling

| Method | Code | Kỹ Thuật | Mô Tả |
|--------|------|----------|-------|
| **I0** | None | Không xử lý | Baseline |
| **I1** | SMOTE + Undersampling | Oversampling minority + Undersampling majority | Target ratio: 33% |
| **I2** | Class Weights | `class_weight='balanced'` | Tự động cân bằng |

### 3. Models

| Model | Hyperparameters |
|-------|-----------------|
| **Logistic Regression** | `max_iter=1000`, `random_state=42` |
| **Random Forest** | `n_estimators=100`, `max_depth=10`, `random_state=42` |
| **Gradient Boosting** | `n_estimators=100`, `max_depth=5`, `random_state=42` |

### 4. Evaluation Metrics

| Metric | Lý Do Chọn |
|--------|------------|
| **ROC-AUC** | Đánh giá khả năng phân biệt tổng thể |
| **PR-AUC** | Tốt cho imbalanced data |
| **F1-Score** | Cân bằng Precision & Recall |
| **Recall** | Quan trọng nhất cho y tế (không bỏ sót bệnh nhân) |
| **Precision** | Độ chính xác của positive predictions |

---

## 📈 Kết Quả

### Tổng Quan Experiments

```
Total Pipelines: 27 (3 Missing × 3 Imbalance × 3 Models)
Models Detecting Stroke: 20/27 (74%)
Models with Recall=0: 7/27 (26%) - Không xử lý imbalance → fail!
```

### Top 5 Pipelines (by ROC-AUC)

| Rank | Pipeline | Model | ROC-AUC | PR-AUC | Recall | F1 |
|------|----------|-------|---------|--------|--------|-----|
| 🥇 1 | M1_I0 | Gradient Boosting | **0.854** | 0.191 | 0.00% | 0.00% |
| 🥈 2 | M1_I2 | Gradient Boosting | 0.854 | 0.191 | 0.00% | 0.00% |
| 🥉 3 | M0_I1 | Logistic Regression | 0.851 | **0.227** | 57.78% | 22.51% |
| 4 | M0_I2 | Logistic Regression | 0.851 | 0.204 | **84.44%** | 21.35% |
| 5 | M0_I0 | Logistic Regression | 0.849 | 0.217 | 0.00% | 0.00% |

### 🏆 Best Models by Criteria

#### 1. Best ROC-AUC (Discriminative Power)
```
Pipeline: M1_I0 + Gradient Boosting
ROC-AUC: 0.8540
⚠️ Warning: Recall = 0% (Cannot detect stroke cases!)
```

#### 2. Best Recall (Medical Priority) ⭐ RECOMMENDED
```
Pipeline: M0_I2 + Logistic Regression
Recall: 84.44%
ROC-AUC: 0.8508
F1-Score: 21.35%
✅ Catches 84% of stroke cases - ideal for medical screening
```

#### 3. Best F1-Score (Balanced)
```
Pipeline: M2_I1 + Random Forest
F1-Score: 27.52%
Recall: 27.78%
ROC-AUC: 0.8232
```

### Key Insights

1. **Imbalance Handling is CRITICAL**
   - Without it (I0): Most models predict all 0 → Recall = 0%
   - Class weights (I2): Best Recall (84%) nhưng precision thấp
   - SMOTE (I1): Cân bằng tốt nhất

2. **Model Complexity Trade-off**
   - Gradient Boosting: Best ROC-AUC nhưng poor recall
   - Logistic Regression: Best recall (simple but effective)
   - Random Forest: Best balance

3. **Missing Data Impact**
   - KNN Imputation (M2) cho F1 tốt hơn
   - Listwise Deletion (M0) vẫn hoạt động tốt với I1/I2

### Top Risk Factors (Feature Importance)

| Rank | Feature | Importance | Insight |
|------|---------|------------|---------|
| 1 | `age` | 0.285 | Tuổi cao → nguy cơ cao |
| 2 | `avg_glucose_level` | 0.262 | Đường huyết cao → nguy cơ |
| 3 | `bmi` | 0.198 | Béo phì → tăng nguy cơ |
| 4 | `hypertension` | 0.089 | Cao huyết áp |
| 5 | `heart_disease` | 0.067 | Bệnh tim |

---

## 🚀 Hướng Dẫn Chạy

### Yêu Cầu Hệ Thống
- Python 3.10+
- 4GB RAM (khuyến nghị 8GB)
- ~500MB disk space

### Cài Đặt

```bash
# 1. Clone repository
git clone https://github.com/Thaianng/Data-Governance-Visualization.git
cd Data-Governance-Visualization

# 2. Tạo virtual environment
python -m venv .venv

# 3. Activate environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 4. Cài đặt dependencies
pip install -r requirements.txt
```

### Chạy Notebooks

Chạy tuần tự các notebooks trong VS Code hoặc Jupyter:

```
1️⃣ 01_data_collection.ipynb      → Load & explore data
2️⃣ 02_data_fusion_cleaning.ipynb → Merge & handle missing data
3️⃣ 03_eda_visualization.ipynb    → EDA & charts
4️⃣ 04_modeling.ipynb             → Train & evaluate models
```

### Output Files

Sau khi chạy xong, các files sẽ được lưu tại:
- `data/processed/` - Processed datasets
- `results/figures/` - All visualizations (17 files)
- `results/models/` - Trained models & summary

---

## 🎯 Kết Luận

### Achievements

✅ **Data Collection**: Thu thập từ 3 nguồn, merge thành 5,610 records  
✅ **Data Quality**: Xử lý 5.22% missing values với 3 phương pháp  
✅ **Imbalance Handling**: So sánh 3 kỹ thuật, I2 cho recall tốt nhất  
✅ **Modeling**: Train 27 pipelines, đạt ROC-AUC 0.854  
✅ **Visualization**: 17 biểu đồ phân tích chi tiết  

### Recommendations

🏥 **Cho ứng dụng Y tế (Screening)**:
- Sử dụng **M0_I2 + Logistic Regression**
- Recall 84.44% - phát hiện được 84% ca đột quỵ
- Chấp nhận false positive rate cao để không bỏ sót bệnh nhân

📊 **Cho ứng dụng Research**:
- Sử dụng **M2_I1 + Random Forest**
- F1 = 27.52% - cân bằng precision/recall
- ROC-AUC = 0.82 - discriminative power tốt

### Limitations & Future Work

1. **Data Size**: Dataset nhỏ (5,610 records) → có thể overfitting
2. **Feature Engineering**: Có thể tạo thêm interaction features
3. **Advanced Models**: Thử XGBoost, LightGBM, Neural Networks
4. **Threshold Tuning**: Optimize decision threshold cho từng use case
5. **External Validation**: Test trên dataset khác

---

## 👥 Thông Tin Nhóm

- **Repository**: [Data-Governance-Visualization](https://github.com/Thaianng/Data-Governance-Visualization)
- **Branch**: `nhdang`

---

## 📚 References

1. [Stroke Prediction Dataset - Kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
2. [Stroke Prediction Dataset - HuggingFace](https://huggingface.co/datasets/jmfilho/stroke-prediction-dataset)
3. [Imbalanced-learn Documentation](https://imbalanced-learn.org/)
4. [Scikit-learn Documentation](https://scikit-learn.org/)

---

<p align="center">
  <b>📅 Last Updated: December 2024</b><br>
  <i>Made with ❤️ for Data Governance & Visualization Course</i>
</p>
