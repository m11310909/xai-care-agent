from database.models import Base
from database.session import engine

if __name__ == "__main__":
    print("🔧 初始化資料庫中...")
    Base.metadata.create_all(bind=engine)
    print("✅ 資料表建立完成！local.db 已產生")