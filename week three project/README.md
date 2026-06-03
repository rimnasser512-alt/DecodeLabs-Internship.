## ✅ Task 3 — Exploratory Data Analysis (EDA)

### 📂 Dataset
- **Name:** Bank Marketing Dataset (`bank.csv`)
- **Source:** Kaggle
- **Size:** 45,211 rows × 17 columns

### 🎯 Goal
Analyze the cleaned dataset to discover meaningful patterns, trends, and 
insights about customer behavior and deposit subscription likelihood.

### 🔍 What Was Done
- Calculated descriptive statistics for all numeric features
- Analyzed deposit subscription rates across multiple customer segments
- Identified outliers in the balance column
- Examined age distribution patterns by subscription outcome
- Created 4 visualizations saved as `task3_eda_charts.png`
  ### 📊 Key Statistics

| Feature | Mean | Min | Max |
|---|---|---|---|
| Age | 40.9 years | 18 | 95 |
| Balance | $1,362 | -$8,019 | $102,127 |
| Duration | 258 seconds | 0 | 4,918 |
| Campaign Contacts | 2.76 | 1 | 63 |

### 📝 Key Findings

**Deposit Subscription Rate:**
- Only **11.7%** of customers subscribed to the term deposit
- The campaign had a **low overall conversion rate**
- - **Students and retired** customers had the highest subscription rates
- **Blue-collar workers** had the lowest subscription rates
- This suggests targeting specific job groups improves campaign success

**Subscription by Education:**
- Customers with **tertiary (university) education** subscribed the most
- Customers with only **primary education** subscribed the least
- Higher financial literacy correlates with greater investment interest

**Subscription by Marital Status:**
- **Single customers** subscribed at the highest rate
- **Married customers** subscribed the least — likely due to more 
  financial obligations

  **Age Distribution:**
- Customers **under 30 and over 60** showed the highest subscription rates
- The **30–50 age group** had the lowest rates — likely due to mortgages 
  and family expenses

**Balance & Outliers:**
- Customers who subscribed had **noticeably higher account balances**
- **Balance outliers** found above $50,000 — kept as valid premium clients
- Financial stability is a **strong predictor** of subscription likelihood

### 📈 Visualizations Generated
1. Deposit Subscription Count (bar chart)
2. Deposit Rate by Education Level (bar chart)
3. Age Distribution by Deposit Subscription (histogram)
4. Account Balance vs Deposit Subscription (box plot)

   
### 🛠️ Libraries Used
- `pandas` — data analysis and grouping
- `numpy` — statistical calculations
- `matplotlib` — chart creation
- `seaborn` — advanced visualizations

---

## 🗂️ Repository Structure
- The dataset is heavily imbalanced — 88.3% said No

**Subscription by Job:**
