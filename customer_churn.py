
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load customer dataset
df = pd.read_csv("data/customer_data.csv")

print("CUSTOMER DATA")
print(df)

# Remove duplicate records
df = df.drop_duplicates()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Calculate total customers
total_customers = len(df)

# Calculate churned customers
churned_customers = (df["Churn"] == "Yes").sum()

# Calculate churn rate
churn_rate = (churned_customers / total_customers) * 100

print("\nCUSTOMER CHURN ANALYSIS")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")

# Analyze churn by contract
print("\nChurn by Contract:")
print(pd.crosstab(df["Contract"], df["Churn"]))

# Create output folder
os.makedirs("output", exist_ok=True)

# Create churn chart
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Analysis")
plt.xlabel("Customer Churn")
plt.ylabel("Number of Customers")
plt.savefig("output/churn_chart.png")
plt.show()

# Save analysis results
df.to_csv("output/customer_churn_results.csv", index=False)

print("\nCustomer Churn Analysis Completed Successfully!")
