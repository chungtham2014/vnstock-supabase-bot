import os
from vnstock_data import Market
from supabase import create_client

# Lấy thông tin bảo mật từ môi trường GitHub
url = os.environ.get("https://inwsknpisxuetmaxqrkg.supabase.co")
key = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlud3NrbnBpc3h1ZXRtYXhxcmtnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyODQyOTcsImV4cCI6MjA4Mjg2MDI5N30.PYydi5HrlP7nRcxB6q1UuBaLPrXyrDVG2HgH_OQnDpA")
supabase = create_client(url, key)

def run_sync():
    mkt = Market()
    # Ví dụ lấy dữ liệu mã VIC
    df = mkt.equity("VIC").ohlcv(start="2026-02-01", end="2026-03-01")

    if not df.empty:
        # Reset index để đưa cột 'time' ra ngoài nếu nó đang là index
        data = df.reset_index().to_dict(orient='records')
        # Upsert vào bảng 'stock_ohlcv'
        supabase.table("stock_ohlcv").upsert(data).execute()
        print("Đã cập nhật dữ liệu thành công!")

if __name__ == "__main__":
    run_sync()
