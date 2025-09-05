from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Kết nối database (tạm thời để cứng, sau này đưa vào config .env)
DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/retail"

# Tạo engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Tạo SessionLocal (mỗi request 1 session)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base cho các model kế thừa
Base = declarative_base()

# Dependency để inject vào router
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
