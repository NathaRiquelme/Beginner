# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset into a pandas DataFrame
file_path = "C:/Users/User/Pictures/beginner/train.csv"
df = pd.read_csv(file_path)

# View the data types of all columns
print(df.dtypes).sum()

# Generate summary statistics using the describe() function
summary_stats = df.describe()
print(summary_stats)

# Identify missing values
"""To identify missing values in the dataset, you can use the isnull() function to create a Boolean DataFrame that indicates True for missing values and False otherwise. Then, you can use the sum() function to calculate the total number of missing values for each column"""
missing_values = df.select_dtypes(include=["number"]).isnull().sum()
print(missing_values)

missing_values = df.select_dtypes(include=["object"]).isnull().sum()
print(missing_values)

# Histogram
plt.hist(df["LotFrontage"], bins=30)
plt.xlabel("LotFrontage")
plt.ylabel("Frequency")
plt.title("Distribution of LotFrontage")
plt.show()

plt.hist(df["LotArea"], bins=30)
plt.xlabel("LotArea")
plt.ylabel("Frequency")
plt.title("Distribution of LotArea")
plt.show()

plt.hist(df["OverallQual"], bins=30)
plt.xlabel("OverallQual")
plt.ylabel("Frequency")
plt.title("Distribution of OverallQual")
plt.show()

plt.hist(df["OverallCond"], bins=30)
plt.xlabel("OverallCond")
plt.ylabel("Frequency")
plt.title("Distribution of OverallCond")
plt.show()

plt.hist(df["YearBuilt"], bins=30)
plt.xlabel("YearBuilt")
plt.ylabel("Frequency")
plt.title("Distribution of YearBuilt")
plt.show()

plt.hist(df["YearRemodAdd"], bins=30)
plt.xlabel("YearRemodAdd")
plt.ylabel("Frequency")
plt.title("Distribution of YearRemodAdd")
plt.show()

plt.hist(df["BsmtFinSF1"], bins=30)
plt.xlabel("BsmtFinSF1")
plt.ylabel("Frequency")
plt.title("Distribution of BsmtFinSF1")
plt.show()

plt.hist(df["BsmtFinSF2"], bins=30)
plt.xlabel("BsmtFinSF2")
plt.ylabel("Frequency")
plt.title("Distribution of BsmtFinSF2")
plt.show()

plt.hist(df["BsmtUnfSF"], bins=30)
plt.xlabel("BsmtUnfSF")
plt.ylabel("Frequency")
plt.title("Distribution of BsmtUnfSF")
plt.show()

plt.hist(df["TotalBsmtSF"], bins=30)
plt.xlabel("TotalBsmtSF")
plt.ylabel("Frequency")
plt.title("Distribution of TotalBsmtSF")
plt.show()

plt.hist(df["1stFlrSF"], bins=30)
plt.xlabel("1stFlrSF")
plt.ylabel("Frequency")
plt.title("Distribution of 1stFlrSF")
plt.show()

plt.hist(df["2ndFlrSF"], bins=30)
plt.xlabel("2ndFlrSF")
plt.ylabel("Frequency")
plt.title("Distribution of 2ndFlrSF")
plt.show()

plt.hist(df["LowQualFinSF"], bins=30)
plt.xlabel("LowQualFinSF")
plt.ylabel("Frequency")
plt.title("Distribution of LowQualFinSF")
plt.show()

plt.hist(df["GrLivArea"], bins=30)
plt.xlabel("GrLivArea")
plt.ylabel("Frequency")
plt.title("Distribution of GrLivArea")
plt.show()

plt.hist(df["BsmtFullBath"], bins=30)
plt.xlabel("BsmtFullBath")
plt.ylabel("Frequency")
plt.title("Distribution of BsmtFullBath")
plt.show()

plt.hist(df["BsmtHalfBath"], bins=30)
plt.xlabel("BsmtHalfBath")
plt.ylabel("Frequency")
plt.title("Distribution of BsmtHalfBath")
plt.show()

plt.hist(df["FullBath"], bins=30)
plt.xlabel("FullBath")
plt.ylabel("Frequency")
plt.title("Distribution of FullBath")
plt.show()

plt.hist(df["HalfBath"], bins=30)
plt.xlabel("HalfBath")
plt.ylabel("Frequency")
plt.title("Distribution of HalfBath")
plt.show()

plt.hist(df["BedroomAbvGr"], bins=30)
plt.xlabel("BedroomAbvGr")
plt.ylabel("Frequency")
plt.title("Distribution of BedroomAbvGr")
plt.show()

plt.hist(df["KitchenAbvGr"], bins=30)
plt.xlabel("KitchenAbvGr")
plt.ylabel("Frequency")
plt.title("Distribution of KitchenAbvGr")
plt.show()

plt.hist(df["TotRmsAbvGrd"], bins=30)
plt.xlabel("TotRmsAbvGrd")
plt.ylabel("Frequency")
plt.title("Distribution of TotRmsAbvGrd")
plt.show()

plt.hist(df["Fireplaces"], bins=30)
plt.xlabel("Fireplaces")
plt.ylabel("Frequency")
plt.title("Distribution of Fireplaces")
plt.show()

plt.hist(df["GarageYrBlt"], bins=30)
plt.xlabel("GarageYrBlt")
plt.ylabel("Frequency")
plt.title("Distribution of GarageYrBlt")
plt.show()

plt.hist(df["GarageCars"], bins=30)
plt.xlabel("GarageCars")
plt.ylabel("Frequency")
plt.title("Distribution of GarageCars")
plt.show()

plt.hist(df["GarageArea"], bins=30)
plt.xlabel("GarageArea")
plt.ylabel("Frequency")
plt.title("Distribution of GarageArea")
plt.show()

plt.hist(df["WoodDeckSF"], bins=30)
plt.xlabel("WoodDeckSF")
plt.ylabel("Frequency")
plt.title("Distribution of WoodDeckSF")
plt.show()

plt.hist(df["OpenPorchSF"], bins=30)
plt.xlabel("OpenPorchSF")
plt.ylabel("Frequency")
plt.title("Distribution of OpenPorchSF")
plt.show()

plt.hist(df["EnclosedPorch"], bins=30)
plt.xlabel("EnclosedPorch")
plt.ylabel("Frequency")
plt.title("Distribution of EnclosedPorch")
plt.show()

plt.hist(df["3SsnPorch"], bins=30)
plt.xlabel("3SsnPorch")
plt.ylabel("Frequency")
plt.title("Distribution of 3SsnPorch")
plt.show()

plt.hist(df["ScreenPorch"], bins=30)
plt.xlabel("ScreenPorch")
plt.ylabel("Frequency")
plt.title("Distribution of ScreenPorch")
plt.show()

plt.hist(df["PoolArea"], bins=30)
plt.xlabel("PoolArea")
plt.ylabel("Frequency")
plt.title("Distribution of PoolArea")
plt.show()

plt.hist(df["MiscVal"], bins=30)
plt.xlabel("MiscVal")
plt.ylabel("Frequency")
plt.title("Distribution of MiscVal")
plt.show()

plt.hist(df["MoSold"], bins=30)
plt.xlabel("MoSold")
plt.ylabel("Frequency")
plt.title("Distribution of MoSold")
plt.show()

plt.hist(df["YrSold"], bins=30)
plt.xlabel("YrSold")
plt.ylabel("Frequency")
plt.title("Distribution of YrSold")
plt.show()

plt.hist(df["YrSold"], bins=30)
plt.xlabel("YrSold")
plt.ylabel("Frequency")
plt.title("Distribution of YrSold")
plt.show()

# Scatter plot
plt.scatter(df["OverallQual"], df["SalePrice"])
plt.xlabel("OverallQual")
plt.ylabel("SalePrice")
plt.title("Relationship between OverallQual and SalePrice")
plt.show()

plt.scatter(df["GrLivArea"], df["SalePrice"])
plt.xlabel("GrLivArea")
plt.ylabel("SalePrice")
plt.title("Relationship between GrLivArea and SalePrice")
plt.show()

plt.scatter(df["TotRmsAbvGrd"], df["SalePrice"])
plt.xlabel("TotRmsAbvGrd")
plt.ylabel("SalePrice")
plt.title("Relationship between TotRmsAbvGrd and SalePrice")
plt.show()

plt.scatter(df["GarageArea"], df["SalePrice"])
plt.xlabel("GarageArea")
plt.ylabel("SalePrice")
plt.title("Relationship between GarageArea and SalePrice")
plt.show()

plt.scatter(df["YearBuilt"], df["SalePrice"])
plt.xlabel("YearBuilt")
plt.ylabel("SalePrice")
plt.title("Relationship between YearBuilt and SalePrice")
plt.show()

plt.scatter(df["LotArea"], df["SalePrice"])
plt.xlabel("LotArea")
plt.ylabel("SalePrice")
plt.title("Relationship between LotArea and SalePrice")
plt.show()

plt.scatter(df["OverallCond"], df["SalePrice"])
plt.xlabel("OverallCond")
plt.ylabel("SalePrice")
plt.title("Relationship between OverallCond and SalePrice")
plt.show()

# Box plot of a categorical feature against a numerical feature
plt.figure(figsize=(8, 6))
sns.boxplot(x="OverallQual", y="SalePrice", data=df)
plt.xlabel("Overall Quality")
plt.ylabel("SalePrice")
plt.title("Distribution of Sale Price by Overall Quality")
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x="MSSubClass", y="SalePrice", data=df)
plt.xlabel("MSSubClass")
plt.ylabel("SalePrice")
plt.title("Distribution of Sale Price by MSSubClass")
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x="MSZoning", y="SalePrice", data=df)
plt.xlabel("MSZoning")
plt.ylabel("SalePrice")
plt.title("Distribution of Sale Price by MSZoning")
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x="Street", y="SalePrice", data=df)
plt.xlabel("Street")
plt.ylabel("SalePrice")
plt.title("Distribution of Sale Price by Street")
plt.show()

# Bar plots
sns.countplot(x="MSSubClass", data=df)
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Bar Plot of MSSubClass")
plt.show()

# Box plot to identify outliers
sns.boxplot(x=df["SalePrice"])
plt.title("Box Plot of Sale Price")
plt.show()

sns.boxplot(x=df["MoSold"])
plt.title("Box Plot of MoSold")
plt.show()

sns.boxplot(x=df["YrSold"])
plt.title("Box Plot of YrSold")
plt.show()

# Assuming 'df' is your DataFrame with the two numerical features

# Select the two numerical columns
numerical_features = df[
    ["YrSold", "SalePrice", "OverallQual", "OverallCond", "YearBuilt", "LotArea"]
]

# Compute the correlation matrix
correlation_matrix = numerical_features.corr()

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
