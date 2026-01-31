import yfinance as yf
from datetime import datetime

def get_market_summary():
    # List of stocks to track (Nifty 50 giants)
    stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS"]
    
    print(f"--- Market Summary ({datetime.now().strftime('%Y-%m-%d %H:%M')}) ---")
    print(f"{'Ticker':<12} | {'Price':<10} | {'Change %':<10}")
    print("-" * 35)

    for ticker in stocks:
        try:
            data = yf.Ticker(ticker)
            # Get the last two days of data to calculate change
            hist = data.history(period="2d")
            if len(hist) < 2:
                continue
            
            current_price = hist['Close'].iloc[-1]
            prev_price = hist['Close'].iloc[-2]
            change = ((current_price - prev_price) / prev_price) * 100
            
            color_symbol = "▲" if change > 0 else "▼"
            print(f"{ticker:<12} | {current_price:>10.2f} | {color_symbol} {change:>8.2f}%")
        except Exception as e:
            print(f"Could not fetch {ticker}: {e}")

if __name__ == "__main__":
    get_market_summary()