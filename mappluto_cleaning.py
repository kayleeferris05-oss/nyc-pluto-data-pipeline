import pandas as pd

# Load the correct file with proper encoding
df = pd.read_csv("pluto_26v2.csv", encoding='latin-1', low_memory=False)

print("Dataset loaded successfully!")
print("Shape of the dataset (Rows, Columns):")
print(df.shape)

print("\nFirst 3 rows of data:")
print(df.head(3))

# Check for missing values in the top columns
print("\n--- Top Missing Values ---")
print(df.isnull().sum().sort_values(ascending=False).head(5))

# Check for any duplicate rows
print("\n--- Duplicate Rows Count ---")
print(df.duplicated().sum())

# Drop columns that are mostly empty (>90% null) ---
threshold = len(df) * 0.90
cols_to_drop = [col for col in df.columns if df[col].isnull().sum() > threshold]

df_cleaned = df.drop(columns=cols_to_drop)

print(f"\n--- Cleaning Action: Dropped Empty Columns ---")
print(f"Removed {len(cols_to_drop)} columns with >90% missing data.")
print(f"New Shape: {df_cleaned.shape}")

# Standardize string columns (strip whitespace) ---
string_cols = df_cleaned.select_dtypes(include=['object']).columns
for col in string_cols:
    df_cleaned[col] = df_cleaned[col].astype(str).str.strip()

print("\n--- Cleaning Action: String Whitespace Cleaned ---")
print(f"Trimmed excess spaces in {len(string_cols)} text fields.")

# Export Cleaned Dataset ---
output_filename = "pluto_cleaned.csv"
df_cleaned.to_csv(output_filename, index=False)

print(f"\n--- Pipeline Complete ---")
print(f"Cleaned dataset saved successfully as '{output_filename}'")
print(f"Final dimensions: {df_cleaned.shape[0]} rows, {df_cleaned.shape[1]} columns.")


import matplotlib.pyplot as plt

# sGenerate Exploratory Data Visualization ---
# Count properties per borough
borough_counts = df_cleaned['borough'].value_counts()

# Create a clean bar chart
plt.figure(figsize=(9, 5))
borough_counts.plot(kind='bar', color='#2b5c8f', edgecolor='black', width=0.6)

plt.title('NYC Tax Lot Distribution by Borough', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Borough', fontsize=12)
plt.ylabel('Number of Tax Lots', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot image for your portfolio
plt.tight_layout()
plt.savefig('borough_distribution.png', dpi=300)
plt.show()

print("Visualization generated and saved as 'borough_distribution.png'!")
