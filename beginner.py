# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset into a pandas DataFrame
file_path = "C:/Users/User/Pictures/beginner/test.csv"
df = pd.read_csv(file_path)

# Generate summary statistics using the describe() function
summary_stats = df.describe()
print(summary_stats)

# Identify missing values
'''To identify missing values in the dataset, you can use the isnull() function to create a Boolean DataFrame that indicates True for missing values and False otherwise. Then, you can use the sum() function to calculate the total number of missing values for each column'''
missing_values = df.isnull().sum()
print(missing_values)

# Histograms
plt.hist(df["OverallCond"])
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of OverallCond")
plt.show()

# Scatter Plots
plt.scatter(df["OverallCond"], df["OverallQual"])
plt.xlabel("OverallCond")
plt.ylabel("OverallQual")
plt.title("Scatter Plot of OverallCond vs OverallQual")
plt.show()