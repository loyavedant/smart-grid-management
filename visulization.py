import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Plot power usage trends
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['power_usage'], label="Power Usage (kWh)", color='blue', marker='o')
plt.xlabel("Index")
plt.ylabel("Power Usage (kWh)")
plt.title("Electricity Demand Over Time")
plt.legend()
plt.show()
