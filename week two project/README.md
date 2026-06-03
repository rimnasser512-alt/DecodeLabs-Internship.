## ✅ Task 2 — Data Cleaning & Preprocessing

### 📂 Dataset
- **Name:** Bank Marketing Dataset (`bank.csv`)
- **Source:** Kaggle
- **Size:** 45,211 rows × 17 columns

### 🎯 Goal
Prepare the dataset for analysis by identifying and fixing all data quality 
issues including missing values, duplicates, and incorrect formatting.

### 🔍 What Was Done
- Loaded the dataset and inspected all columns for quality issues
- Detected hidden missing values disguised as the string `"unknown"`
- Applied appropriate filling strategies per column
- Checked for and confirmed zero duplicate records
  - Converted binary text columns from yes/no to numeric 0/1
- Fixed the `pdays` column where -1 meant "never contacted"
- Saved the cleaned dataset as `bank_cleaned.csv`

### 🧹 Cleaning Steps Applied

| Issue Found | Column(s) Affected | Action Taken |
|---|---|---|
| 'unknown' string values | job (288), education (1857) | Replaced with most common value (mode) |
| 'unknown' string values | contact (13,020), poutcome (36,959) | Labeled as 'not_available' |
| Binary text (yes/no) | default, housing, loan, deposit | Converted to numeric 0 and 1 |
| Invalid -1 values | pdays | Replaced with 0 (means never contacted) |
| Duplicate records | All columns | None found — dataset already clean |
| Negative balances | balance | Kept — valid overdraft accounts (3,766) |

### 📝 Key Findings
- No traditional NaN missing values existed — missing data was **hidden 
  as the word "unknown"**
- The `poutcome` column had **82% unknown values** making it unreliable 
  for direct analysis
- **3,766 accounts** had negative balances representing valid real-world 
  overdraft situations
- After cleaning the dataset remained at **45,211 rows** with improved 
  data types and no quality issues

### 🛠️ Libraries Used
- `pandas` — data manipulation and cleaning
- `numpy` — handling NaN replacement

---
| Invalid -1 values | pdays | Replaced with 0 (means never contacted) |
| Duplicate records | All columns | None found — dataset already clean |
| Negative balances | balance | Kept — valid overdraft accounts (3,766) |
