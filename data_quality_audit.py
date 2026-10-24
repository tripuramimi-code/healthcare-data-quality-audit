import pandas as pd

df = pd.read_csv('healthcare_dataset.csv')

print("--- FIRST 5 ROWS OF DATA ---")
print(df.head())

print("/n--- DATA TYPES AND COLUMN INFO ---")
print(df.info())

# Step 4:  Data quality Audit (Find Bugs)
print("/n=== STARTING DATA QUALITY AUDIT ===")

#Check for missing values (conpleteness)
missing_counts = df.isnull().sum()
print("/n[!] Missing Values Per Column:")
print(missing_counts)

#Check the duplicate Rows (Uniqueness)
duplicate_count = df.duplicated().sum()
print(f"/n[!] Total Duplicate Records Found: {duplicate_count}")

# Step 5: The Cleaning Phase (Fix Bugs)
print("/n=== STARTING CLEANING PROCESS ===")

# FIX A: Drop rows where critical data is completely missing
# (we drop rows if they don't even have basic records)
df_clean = df.dropna()

# Fix B Remove duplicates
df_clean = df_clean.drop_duplicates()

print("cleaning complete!")

# Step 6: Export & Generate report
df_clean.to_csv('clean_healthcare_data.csv', index=False)

original_rows = len(df)
clean_rows = len(df_clean)
rows_removed = original_rows - clean_rows

print("/n=== FINAL DATA QUALITY METRICS ===")
print(f"Original Records: {original_rows}")
print(f"Cleaned Record Saved: {clean_rows}")
print(f"Totol Corrupted Rows Removed: {rows_removed}")
print(f"Final Data  Integrity Score: {round(clean_rows / original_rows * 100, 2)}%")
