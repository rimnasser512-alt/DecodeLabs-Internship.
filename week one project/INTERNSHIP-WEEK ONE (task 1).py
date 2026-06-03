import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =====================
# Load the Dataset
# =====================
df = pd.read_csv(r"C:\Users\rimna\OneDrive\Desktop\canser.csv")

# =====================
# 1. Dataset Size
# =====================
print("=== Dataset Shape (rows, columns) ===")
print(df.shape)

# =====================
# 2. Column Names & Data Types
# =====================
print("\n=== Column Names and Data Types ===")
print(df.dtypes)

# =====================
# 3. First Look at Data
# =====================
print("\n=== First 5 Rows ===")
print(df.head())

# =====================
# 4. Missing Values
# =====================
print("\n=== Missing Values Per Column ===")
print(df.isnull().sum())

# =====================
# 5. Basic Statistics
# =====================
print("\n=== Basic Statistics ===")
print(df.describe())

print("\n✅ Task 1 Complete!")