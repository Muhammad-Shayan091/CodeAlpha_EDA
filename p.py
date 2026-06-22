# ============================================================
# NETFLIX EDA PROJECT
# Libraries used: pandas & numpy ONLY (for data work)
# matplotlib is used ONLY for charts — no data logic in it
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# ===================
# STEP 1: LOAD DATA
# ===================
df = pd.read_csv('netflix_titles.csv')

print("=" * 55)
print("STEP 1: DATA LOADED")
print("=" * 55)

# ======================
# NO OF ROWS AND COLUMNS
# ======================
print(f"Rows    : {df.shape[0]}")                      
print(f"Columns : {df.shape[1]}")                       

# ============================
# LIST OF COLUMNS IN THE DATA
# ============================
print(f"\nColumn Names:\n{df.columns.tolist()}")

# =======================
# PRINTING FIRST "n" ROWS
# =======================
print(f"\nFirst 3 rows:")
print(df.head(3))


# ======================
# STEP 2: DATA OVERVIEW
# ======================
print("\n" + "=" * 55)
print("STEP 2: DATA OVERVIEW")
print("=" * 55)
print(df.dtypes)
missing = df.isnull().sum()
missing_pct = np.round((missing / len(df)) * 100, 2)

# pd.DataFrame() builds a new table from a dictionary
missing_table = pd.DataFrame({
    'Missing Count': missing,
    'Missing %'    : missing_pct
})

print("\nMissing Values Per Column:")
print(missing_table[missing_table['Missing Count'] > 0])

# =====================
# STEP 3: DATA CLEANING
# =====================
print("\n" + "=" * 55)
print("STEP 3: DATA CLEANING")
print("=" * 55)

# FILL MISSING TEXT WITH PLACEHOLDER
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)

# CHECKING DUPLICATES VALUES
dupes = df.duplicated().sum()   
print(f"Duplicate rows found: {dupes}")
df.drop_duplicates(inplace=True)

# CONVERT TEXT TO REAL-DATE
df['date_added'] = df['date_added'].str.strip()
df['date_added_parsed'] = pd.to_datetime(df['date_added'], errors='coerce')

# PULL (YEAR , MONTH , DAY) FROM THE REAL_DATE 
df['year_added']  = df['date_added_parsed'].dt.year
df['month_added'] = df['date_added_parsed'].dt.month
df['year_added']  = df['date_added_parsed'].dt.day

# print("Cleaning done!")
print(f"Remaining rows after cleaning: {len(df)}")


