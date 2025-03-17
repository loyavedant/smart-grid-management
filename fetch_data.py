import mysql.connector
import pandas as pd


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Loya@4112", 
    database="smart_grid_db"
)


query = "SELECT * FROM electricity_demand"
df = pd.read_sql(query, conn)

df.to_csv("electricity_data.csv", index=False)
print(" Data saved to electricity_data.csv")

conn.close()
