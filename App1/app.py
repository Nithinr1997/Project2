import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create mock data with random values
np.random.seed(42)
date_range = pd.date_range(start="1992-01-01", end="1992-10-20")  # Simulate 293 days
sales_data = pd.DataFrame({
    "ds": date_range,
    "y": np.random.randint(100, 500, size=len(date_range))  # Random sales values
})

# Read the dataset
print("Dataset Head:")
print(sales_data.head())

# Check for missing values
print("\nMissing Values:")
print(sales_data.isnull().sum())

# Visualize the time series
plt.figure(figsize=(10, 6))
plt.plot(sales_data["ds"], sales_data["y"], label="Daily Sales", color="orange")
plt.title("Retail Sales Time Series")
plt.xlabel("Date")
plt.ylabel("Sales (USD)")
plt.legend()
plt.show()
