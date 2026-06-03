import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =====================
# Load the Dataset
# =====================
df = pd.read_csv("bank.csv")

# =====================
# Apply Basic Cleaning First
# =====================
df[['job', 'education', 'contact', 'poutcome']] = df[['job', 'education', 'contact', 'poutcome']].replace('unknown', np.nan)
df['job'].fillna(df['job'].mode()[0], inplace=True)
df['education'].fillna(df['education'].mode()[0], inplace=True)
df['contact'].fillna('not_available', inplace=True)
df['poutcome'].fillna('not_available', inplace=True)
df['pdays'] = df['pdays'].replace(-1, 0)
binary_cols = ['default', 'housing', 'loan', 'deposit']
for col in binary_cols:
    df[col] = df[col].map({'yes': 1, 'no': 0})

# =====================
# 1. Basic Statistics
# =====================
print("=== Basic Statistics ===")
print(df.describe())

# =====================
# 2. Deposit Subscription Rate
# =====================
print("\n=== Deposit Subscription Rate ===")
print(df['deposit'].value_counts())
print(f"Subscription Rate: {df['deposit'].mean()*100:.1f}%")

# =====================
# 3. Average Age & Balance
# =====================
print("\n=== Average Age ===")
print(f"Mean Age: {df['age'].mean():.1f} years")
print(f"Median Age: {df['age'].median():.1f} years")

print("\n=== Balance Statistics ===")
print(f"Mean Balance: ${df['balance'].mean():.2f}")
print(f"Median Balance: ${df['balance'].median():.2f}")
print(f"Negative Balances (overdraft): {(df['balance'] < 0).sum()}")

# =====================
# 4. Deposit Rate by Job
# =====================
print("\n=== Deposit Rate by Job ===")
print(df.groupby('job')['deposit'].mean().sort_values(ascending=False))

# =====================
# 5. Deposit Rate by Education
# =====================
print("\n=== Deposit Rate by Education ===")
print(df.groupby('education')['deposit'].mean().sort_values(ascending=False))

# =====================
# 6. Deposit Rate by Marital Status
# =====================
print("\n=== Deposit Rate by Marital Status ===")
print(df.groupby('marital')['deposit'].mean().sort_values(ascending=False))

# =====================
# 7. Outliers in Balance
# =====================
mean_bal = df['balance'].mean()
std_bal = df['balance'].std()
outliers = df[df['balance'] > mean_bal + 3*std_bal]
print(f"\n=== Balance Outliers (very high balance) ===")
print(f"Number of outliers: {len(outliers)}")
print(f"Minimum outlier balance: ${outliers['balance'].min():.2f}")
print(f"Maximum outlier balance: ${outliers['balance'].max():.2f}")

# =====================
# 8. Visualizations
# =====================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Bank Marketing EDA — Key Insights', 
             fontsize=16, fontweight='bold')

# Chart 1 — Deposit Subscription Count
sns.countplot(data=df, x='deposit', palette='Set2', ax=axes[0,0])
axes[0,0].set_title('Deposit Subscription (0=No, 1=Yes)')
axes[0,0].set_xlabel('Subscribed to Deposit')

# Chart 2 — Deposit Rate by Education
edu_data = df.groupby('education')['deposit'].mean().sort_values(ascending=False)
axes[0,1].bar(edu_data.index, edu_data.values, color='steelblue')
axes[0,1].set_title('Deposit Rate by Education Level')
axes[0,1].set_ylabel('Subscription Rate')
axes[0,1].set_xlabel('Education')

# Chart 3 — Age Distribution by Deposit
sns.histplot(data=df, x='age', hue='deposit', bins=30, ax=axes[1,0])
axes[1,0].set_title('Age Distribution by Deposit Subscription')
axes[1,0].set_xlabel('Age')

# Chart 4 — Balance by Deposit
sns.boxplot(data=df, x='deposit', y='balance', palette='Set1', ax=axes[1,1])
axes[1,1].set_title('Account Balance vs Deposit Subscription')
axes[1,1].set_xlabel('Subscribed (0=No, 1=Yes)')
axes[1,1].set_ylabel('Balance ($)')

plt.tight_layout()
plt.savefig("task3_eda_charts.png", dpi=150)
plt.show()
print("\n✅ Task 3 Complete!")
print("✅ Charts saved as task3_eda_charts.png!")