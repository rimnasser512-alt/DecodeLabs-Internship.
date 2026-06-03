import pandas as pd
import numpy as np


df = pd.read_csv("bank.csv")

print("=== Original Shape ===")
print(df.shape)


print("\n=== Missing Values (NaN) ===")
print(df.isnull().sum())

unknown_cols = ['job', 'education', 'contact', 'poutcome']

for col in unknown_cols:
    count = (df[col] == 'unknown').sum()
    print(f"\n'unknown' values in '{col}': {count}")


df[unknown_cols] = df[unknown_cols].replace('unknown', np.nan)


df['job'].fillna(df['job'].mode()[0], inplace=True)
df['education'].fillna(df['education'].mode()[0], inplace=True)


df['contact'].fillna('not_available', inplace=True)
df['poutcome'].fillna('not_available', inplace=True)

print("\n=== After Handling Unknowns ===")
print(df[unknown_cols].isnull().sum())


print(f"\n=== Duplicates Before: {df.duplicated().sum()} ===")
df.drop_duplicates(inplace=True)
print(f"=== Duplicates After: {df.duplicated().sum()} ===")


print(f"\npdays = -1 count (never contacted): {(df['pdays'] == -1).sum()}")
df['pdays'] = df['pdays'].replace(-1, 0)
print("pdays -1 replaced with 0 ✅")


binary_cols = ['default', 'housing', 'loan', 'deposit']
for col in binary_cols:
    df[col] = df[col].map({'yes': 1, 'no': 0})
    print(f"{col} converted to 0/1 ✅")


month_order = ['jan','feb','mar','apr','may','jun',
               'jul','aug','sep','oct','nov','dec']
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
print("month converted to ordered category ✅")


neg_balance = (df['balance'] < 0).sum()
print(f"\nNegative balance accounts: {neg_balance} (kept — valid overdrafts)")


print("\n=== Final Dataset Shape ===")
print(df.shape)

print("\n=== Data Types After Cleaning ===")
print(df.dtypes)

print("\n=== Missing Values After Cleaning ===")
print(df.isnull().sum())


df.to_csv(r"C:\Users\rimna\OneDrive\Desktop\bank_cleaned.csv", index=False)
