# Data Governance & Visualization
## Dự Đoán Nguy Cơ Đột Quỵ Từ Dữ Liệu Y Tế

> **Đề tài:** Dự đoán nguy cơ đột quỵ từ dữ liệu y tế không đầy đủ & mất cân bằng  
> **Kỹ thuật:** Missing Data + Imbalanced Data + Data Fusion + Classification

---

## 📋 Mục Lục
- [1. Phân Công Nhóm](#1-phân-công-nhóm)
- [2. Tìm Hiểu Lý Thuyết](#2-tìm-hiểu-lý-thuyết)
- [3. Thu Thập & Lưu Trữ Dữ Liệu](#3-thu-thập--lưu-trữ-dữ-liệu)
- [4. Tích Hợp & Làm Sạch Dữ Liệu](#4-tích-hợp--làm-sạch-dữ-liệu)
- [5. Xử Lý Mất Cân Bằng](#5-xử-lý-mất-cân-bằng)
- [6. EDA & Trực Quan Hóa](#6-eda--trực-quan-hóa)
- [7. Xây Dựng Mô Hình](#7-xây-dựng-mô-hình)

---

## 1. Phân Công Nhóm

| Nhóm | Nhiệm vụ |
|------|----------|
| **Nhóm 1** | Lý thuyết & đọc tài liệu |
| **Nhóm 2** | Thu thập & xử lý dữ liệu |
| **Nhóm 3** | EDA & visualization |
| **Nhóm 4** | Modeling & viết báo cáo/slide |

---

## 2. Tìm Hiểu Lý Thuyết

### 📚 Các chủ đề cần nghiên cứu:

#### 2.1 Missing Data
- **MCAR** (Missing Completely At Random)
- **MAR** (Missing At Random)
- **MNAR** (Missing Not At Random)
- **Phương pháp xử lý:** Deletion, Mean/Median Imputation, kNN, MICE

#### 2.2 Imbalanced Data
- **Resampling techniques:** SMOTE, Under-sampling, Over-sampling
- **Cost-sensitive learning**

#### 2.3 Data Fusion
- Tích hợp dữ liệu từ nhiều nguồn khác nhau
- Chuẩn hóa và mapping dữ liệu

#### 2.4 Classification Metrics
- **ROC-AUC, PR-AUC**
- **F1-Score, Recall, Precision**
- Đánh giá trên dữ liệu mất cân bằng

### 📝 Deliverable
Chương "Cơ sở lý thuyết" cho báo cáo (4–6 trang)

---

## 3. Thu Thập & Lưu Trữ Dữ Liệu

### 📊 Nguồn dữ liệu

Chọn và tải về **2–3 bộ dữ liệu** từ:
- Kaggle
- Mendeley
- UCI Machine Learning Repository

### 📂 Cấu trúc lưu trữ
```
data/
├── raw/
│   ├── stroke_kaggle.csv
│   ├── stroke_fullfilled.csv
│   └── stroke_synthetic.csv
└── processed/
```

### 📋 Thông tin cần ghi nhận cho mỗi dataset:
- ✅ Link nguồn
- ✅ Mô tả ngắn (số dòng, số cột, biến chính)
- ✅ License

### 🎁 Optional (Cộng điểm)
- Thiết kế **Google Form** khảo sát thói quen sức khỏe
- Thu thập **50–100 bản ghi** từ lớp
- Tạo bộ dữ liệu thực riêng của nhóm

---

## 4. Tích Hợp & Làm Sạch Dữ Liệu

### 4.1 Chuẩn Hóa & Tích Hợp (Data Fusion)

**Các bước thực hiện:**
1. Liệt kê các cột của từng dataset
2. Map các cột cùng ý nghĩa
3. Chuẩn hóa kiểu dữ liệu (numeric/categorical)
4. Chuẩn hóa nhãn stroke về 0/1
5. Ghép các dataset thành 1 bảng lớn
6. Thêm cột `source` để phân biệt nguồn

### 4.2 Phân Tích Missing & Làm Sạch

**Tasks:**
- Tính tỉ lệ missing theo cột
- Vẽ biểu đồ missing (heatmap/matrix)
- Kiểm tra giá trị bất hợp lý/outlier (BMI = 0, glucose < 0, etc.)

### 4.3 Pipeline Xử Lý Missing

| Pipeline | Mô tả | Phương pháp |
|----------|-------|-------------|
| **M0** | Baseline | Listwise deletion (xóa dòng thiếu nhiều) |
| **M1** | Simple Imputation | Mean/Median cho số, Mode cho categorical |
| **M2** | Advanced Imputation | kNN / MICE |

---

## 5. Xử Lý Mất Cân Bằng

### Pipeline Imbalance Handling

| Pipeline | Mô tả | Phương pháp |
|----------|-------|-------------|
| **I0** | Baseline | Không xử lý (giữ phân bố gốc) |
| **I1** | Resampling | SMOTE + Under-sampling |
| **I2** | Cost-sensitive | `class_weight="balanced"` |

### 🔄 Kết hợp Pipelines
- M0 + I0 (Baseline)
- M1 + I1 (Simple + SMOTE)
- M2 + I2 (Advanced + Cost-sensitive)

---

## 6. EDA & Trực Quan Hóa

### 6.1 EDA Tổng Quát

**Biến số (Numeric):**
- Thống kê mô tả (mean, median, std, min, max)
- Histogram/Boxplot cho: `age`, `glucose`, `bmi`

**Biến phân loại (Categorical):**
- Bar chart cho: `gender`, `hypertension`, `heart_disease`, `smoking_status`

### 6.2 Visualization về Missing & Imbalance

- 📊 Biểu đồ tỉ lệ missing
- 📊 Biểu đồ pattern missing
- 📊 Phân bố nhãn stroke (trước & sau xử lý)

### 6.3 EDA Theo Nhãn (Diagnostic Analysis)

**So sánh Stroke vs Non-Stroke:**
- Boxplot/Violin plot cho: `age`, `bmi`, `glucose`
- Bar chart/Stacked bar cho tỉ lệ stroke theo:
  - `hypertension`
  - `heart_disease`
  - `smoking_status`

**Optional:**
- So sánh giữa các nguồn dữ liệu (`source`)

### 📝 Output
Ghi lại **insights chính** từ EDA với storytelling qua đồ thị

---

## 7. Xây Dựng Mô Hình

### 7.1 Lựa Chọn Mô Hình

| Mô hình | Ưu điểm |
|---------|---------|
| **Logistic Regression** | Dễ giải thích, baseline tốt |
| **Random Forest** | Hiệu năng cao, robust |
| **Gradient Boosting** | State-of-the-art performance |

### 7.2 Quy Trình Training & Evaluation

**Cho mỗi pipeline (M* + I*):**

1. **Split data:** Train-test split hoặc Cross-validation
2. **Training:** Fit model trên training set
3. **Evaluation metrics:**
   - ROC-AUC
   - PR-AUC
   - Recall, Precision, F1-Score (class stroke)
4. **Visualization:**
   - ROC Curve
   - Precision-Recall Curve
   - Confusion Matrix

### 7.3 Model Interpretation

**Feature Importance:**
- Feature importance từ tree-based models
- SHAP values (nếu có thời gian)
- Rút ra các yếu tố nguy cơ chính

### 7.4 Tổng Hợp Kết Quả

**Tasks:**
- So sánh các pipeline
- Chọn "best pipeline"
- Phân tích: Xử lý missing + imbalance cải thiện như thế nào?

---

## 📌 Notes
- Tất cả code và notebook cần có comment rõ ràng
- Mỗi visualization cần có title, labels, và interpretation
- Lưu tất cả kết quả vào folder `results/`
- Version control với Git

---

## 📁 Cấu Trúc Project

```
Data-Governance-Visualization/
├── README.md
├── data/
│   ├── raw/                          # Dữ liệu gốc
│   │   ├── stroke_kaggle.csv
│   │   ├── stroke_huggingface.csv
│   │   ├── stroke_synthetic.csv
│   │   └── data_info.json            # Thông tin nguồn dữ liệu
│   └── processed/                    # Dữ liệu đã xử lý
│       ├── stroke_M0.csv             # Listwise deletion
│       ├── stroke_M1.csv             # Median imputation
│       ├── stroke_M2.csv             # KNN imputation
│       ├── stroke_merged_clean.csv
│       └── label_encoders.json
├── notebooks/
│   ├── 01_data_collection.ipynb      # Thu thập & khảo sát dữ liệu
│   ├── 02_data_fusion_cleaning.ipynb # Tích hợp & làm sạch
│   ├── 03_eda_visualization.ipynb    # Phân tích EDA
│   └── 04_modeling.ipynb             # Xây dựng mô hình
├── src/
│   ├── download_data.py              # Script download data
│   └── utils.py                      # Utility functions
└── results/
    ├── figures/                      # Các biểu đồ
    └── models/                       # Mô hình đã train
```

---

## 🚀 Hướng Dẫn Chạy

### 1. Cài đặt môi trường
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn missingno shap datasets
```

### 2. Chạy các notebooks theo thứ tự
1. `01_data_collection.ipynb` - Khảo sát dữ liệu
2. `02_data_fusion_cleaning.ipynb` - Xử lý missing data
3. `03_eda_visualization.ipynb` - EDA & visualization
4. `04_modeling.ipynb` - Train & evaluate models

---

**Last updated:** December 2025
