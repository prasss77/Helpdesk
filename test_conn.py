from sqlalchemy import text
from app.db.session import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Koneksi PostgreSQL berhasil:", result.scalar())

except Exception as exc:
    print("Koneksi PostgreSQL gagal.")
    print(type(exc).__name__, str(exc))

finally:
    engine.dispose()