import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r'C:/Users/ksrut/Downloads/HINDALCO_1D.xlsx' 
df = pd.read_excel(file_path)


df['datetime'] = pd.to_datetime(df['datetime'])
short_window = 50
long_window = 200

df['SMA50'] = df['close'].rolling(window=short_window, min_periods=1).mean()
df['SMA200'] = df['close'].rolling(window=long_window, min_periods=1).mean()

df['Signal'] = 0
df['Signal'][short_window:] = np.where(df['SMA50'][short_window:] > df['SMA200'][short_window:], 1, 0)
df['Position'] = df['Signal'].diff()
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['close'], label='Close Price', color='blue', alpha=0.5)
plt.plot(df.index, df['SMA50'], label='50-Day SMA', color='red', alpha=0.75)
plt.plot(df.index, df['SMA200'], label='200-Day SMA', color='green', alpha=0.75)


plt.plot(df[df['Position'] == 1].index, 
         df['SMA50'][df['Position'] == 1], 
         '^', markersize=10, color='g', lw=0, label='Buy Signal')

plt.plot(df[df['Position'] == -1].index, 
         df['SMA50'][df['Position'] == -1], 
         'v', markersize=10, color='r', lw=0, label='Sell Signal')

plt.title('SMA Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid()
plt.show()
