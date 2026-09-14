import pandas as pd

# Load cleaned apparel dataset
df = pd.read_csv("data/cleaned_apparel_fashion_data.csv")

print("===== DATASET OVERVIEW =====")
print(df.head())
print("\nDataset Shape:", df.shape)

# Numerical summary
print("\n===== NUMERICAL SUMMARY =====")
print(df.describe())

# Category analysis
print("\n===== CATEGORY ANALYSIS =====")
category_count = df["Category"].value_counts()
print(category_count)

# Material analysis
print("\n===== MATERIAL ANALYSIS =====")
material_count = df["Material"].value_counts()
print(material_count)

# Colour analysis
print("\n===== COLOUR ANALYSIS =====")
colour_count = df["Colour"].value_counts()
print(colour_count)

# Average price by category
print("\n===== AVERAGE SALE PRICE BY CATEGORY =====")
avg_price = df.groupby("Category")["Sale_Price"].mean()
print(avg_price)

# Average discount
if "Discount_Percent" in df.columns:
    print("\n===== AVERAGE DISCOUNT =====")
    print(df["Discount_Percent"].mean())

# Average rating by category
print("\n===== AVERAGE RATING BY CATEGORY =====")
avg_rating = df.groupby("Category")["Rating"].mean()
print(avg_rating)

# Correlation analysis
print("\n===== CORRELATION ANALYSIS =====")
numeric_columns = [
    "Original_Price",
    "Sale_Price",
    "Rating",
    "Discount_Percent"
]

available_columns = [
    col for col in numeric_columns if col in df.columns
]

print(df[available_columns].corr())

print("\nEDA analysis completed successfully!")
