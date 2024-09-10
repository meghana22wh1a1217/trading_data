import pandas as pd
import mysql.connector


file_path = r'C:/Users/ksrut/Downloads/HINDALCO_1D.xlsx'

try:
    df = pd.read_excel(file_path)
    print(df.columns)
except Exception as e:
    print(f"An error occurred: {e}")


df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="trading_data"
)
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO stock_data (date, open, high, low, close, volume, datetime)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row['datetime'], row['open'], row['high'], row['low'], row['close'], row['volume'], row['datetime']))


conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully!")
