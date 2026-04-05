import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("insurance.csv")

# Display basic info
print(df.head())
print(df.info())

# Check missing values
print(df.isnull().sum())

# Average charges by smoker
smoker_charges = df.groupby("smoker")["charges"].mean()
print(smoker_charges)

# Visualization
plt.figure()
smoker_charges.plot(kind="bar")
plt.title("Average Insurance Charges: Smoker vs Non-Smoker")
plt.xlabel("Smoker")
plt.ylabel("Charges")
plt.savefig("smoker_charges.png")

# Age vs Charges
plt.figure()
plt.scatter(df["age"], df["charges"])
plt.title("Age vs Insurance Charges")
plt.xlabel("Age")
plt.ylabel("Charges")
plt.savefig("age_vs_charges.png")

print("Analysis Completed")
