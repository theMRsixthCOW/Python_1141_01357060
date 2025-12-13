import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

df = yf.download("NVDA", start="2025-01-01", end="2025-12-01", auto_adjust=True)

if df.empty:
    print("股票數據下載失敗。")

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

if 'Adj Close' in df.columns and 'Close' in df.columns:
    adj = df['Adj Close'] / df['Close']
    for col in ['Open', 'High', 'Low', 'Close']:
        if col in df.columns:
            df[col] = df[col] * adj


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(14, 8))

ax1.set_ylabel('Close Price')
ax1.plot(df.index, df['Close'], color='blue', label='Close Price')
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.set_ylabel('Volume')
ax2.bar(df.index, df['Volume'], alpha=0.5)
ax2.set_xlabel('Date')

plt.tight_layout()
plt.title('NVDA Price and Volume')
fig.autofmt_xdate()
plt.show()
