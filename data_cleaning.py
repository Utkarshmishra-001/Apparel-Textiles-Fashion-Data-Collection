import pandas as pd

# Load dataset
df = pd.read_csv("data/apparel_fashion_data.csv")

print("Original Dataset:")
print(df)

# Remove duplicate records
df = df.drop_duplicates()

# Standardize text columns
df["Category"] = df["Category"].str.strip().str.title()
df["Material"] = df["Material"].str.strip().str.title()
df["Colour"] = df["Colour"].str.strip().str.title()

# Standardize category names
df["Category"] = df["Category"].replace({
    "T Shirt": "T-Shirt"
})

# Convert price columns to numeric
df["Original_Price"] = pd.to_numeric(
    df["Original_Price"], errors="coerce"
)

df["Sale_Price"] = pd.to_numeric(
    df["Sale_Price"], errors="coerce"
)

# Calculate discount percentage
df["Discount_Percent"] = (
    (df["Original_Price"] - df["Sale_Price"])
    / df["Original_Price"]
    * 100
).round(2)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv(
    "data/cleaned_apparel_fashion_data.csv",
    index=False
)

print("\nData cleaning completed successfully!")
print("\nCleaned Dataset:")
print(df)
