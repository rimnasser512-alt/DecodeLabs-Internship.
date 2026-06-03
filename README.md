# DecodeLabs Data Science Internship — Week 1
**Intern:** Rimna  
**Track:** Data Science  
**Organization:** DecodeLabs  

---

## 📌 Overview
This repository contains the Week 1 project tasks completed as part of the 
DecodeLabs Data Science Internship. The tasks cover the full data science 
pipeline — from loading and understanding data, to cleaning it, and finally 
analyzing it to extract real-world insights.

---

## ✅ Task 1 — Data Collection & Dataset Understanding
### 📂 Dataset
- **Name:** Breast Cancer Dataset (`cancer.csv`)
- **Source:** Kaggle
- **Size:** 683 rows × 10 columns

### 🎯 Goal
Load the dataset and fully understand its structure, features, and content 
before any analysis begins.

### 🔍 What Was Done
- Loaded the dataset using the pandas library in Python
- Identified all column names and their data types
- Explored the dataset size and structure
- Checked for missing values across all columns
- Generated basic descriptive statistics

### 📊 Dataset Columns

| Column | Data Type | Description |
|---|---|---|
| Class | int64 | Target variable — 0 = no recurrence, 1 = recurrence |
| age | int64 | Patient age group (encoded numerically) |
| menopause | int64 | Menopause status of the patient |
| tumor-size | int64 | Size of the tumor |
| inv-nodes | int64 | Number of invaded lymph nodes |
| node-caps | int64 | Whether node caps are involved |
| deg-malig | int64 | Degree of malignancy |
| breast | int64 | Which breast is affected |
| breast-quad | int64 | Quadrant of the breast where tumor is located |
| irradiat | int64 | Whether patient received radiation therapy |
### 📝 Key Findings
- The dataset contains **683 patient records** with **10 features** each
- **All columns are integer type** — the dataset uses numerical encoding 
  for all categorical values
- **No missing values** were found in any column
- Approximately **35% of patients** experienced cancer recurrence (Class = 1)
  while **65% did not** (Class = 0)
- All features use a **1–10 numerical scale** meaning original categorical 
  values like age groups and breast quadrants have been pre-encoded
- This dataset is used to predict breast cancer recurrence based on 
  clinical features collected at diagnosis
  ### 🛠️ Libraries Used
- `pandas` — loading and exploring the dataset
- `numpy` — numerical operations
- `matplotlib` — visualization support
- `seaborn` — visualization support
