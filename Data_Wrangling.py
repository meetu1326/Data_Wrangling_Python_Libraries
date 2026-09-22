import os
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

# Set visual style
sns.set_theme(style="whitegrid")

df = pd.read_csv('data.csv')

print("--- 1. Initial Inspection ---")
print("Shape (Rows, Columns):", df.shape)
df.info()
print("\nFirst 5 rows:")
print(df.head())

print("\n--- Missing Values Before Cleaning ---")
print(df.isnull().sum())

drop_values = df.drop_duplicates().head(10)
print(f'drop_values: {drop_values}')
drop = df.dropna().head(10)
print(f'dropna values: {drop}')



# Strategy A: Impute numerical columns with their median/mean
num_cols = df.select_dtypes(include=["number"]).columns
for col in num_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())

# Strategy B: Impute categorical/text columns with mode or 'Unknown'
cat_cols = df.select_dtypes(include=["object"]).columns
for col in cat_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna("Unknown")

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

# Plot 1: Distribution of a numerical column (e.g., first numeric column)
if len(num_cols) > 0:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[num_cols[0]], kde=True, color="royalblue")
    plt.title(f"Distribution of {num_cols[0]}", fontsize=14)
    plt.xlabel(num_cols[0])
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Plot 2: Count plot of a categorical column (e.g., first categorical column)
if len(cat_cols) > 0:
    plt.figure(figsize=(9, 4))
    top_categories = df[cat_cols[0]].value_counts().nlargest(8).index
    sns.countplot(
        data=df[df[cat_cols[0]].isin(top_categories)],
        x=cat_cols[0],
        order=top_categories,
        palette="viridis",
    )
    plt.title(f"Top Counts by {cat_cols[0]}", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ---------------------------------------------------------
# 7. EXPORT CLEANED DATASET
# ---------------------------------------------------------
output_path = os.path.join(base_dir, "Cleaned_Dataset.csv")
df.to_csv(output_path, index=False)
print(f"\nCleaned dataset saved successfully to: {output_path}")