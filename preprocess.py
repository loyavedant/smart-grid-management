import pandas as pd

# Load data from CSV
df = pd.read_csv("electricity_data.csv")

df['timestamp'] = pd.to_datetime(df['timestamp'])


df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek


df.drop(columns=['timestamp'], inplace=True)

df.to_csv("cleaned_data.csv", index=False)

print("Data Preprocessing Complete. Cleaned data saved as cleaned_data.csv")
