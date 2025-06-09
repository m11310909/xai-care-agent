from dotenv import load_dotenv
import os

load_dotenv()

# 試著讀取你 .env 檔案中的一個變數
# 如果你還沒有 LIFF_ID，可以換成 OPENAI_API_KEY 或其他任何你已設定的變數
liff_id = os.getenv("LIFF_ID")

if liff_id:
    print(f"✅ 成功讀取！LIFF_ID 是: {liff_id}")
else:
    print("❌ 讀取失敗！請檢查 .env 檔案是否存在，或變數名稱是否正確。")
