from app.db.session import engine
from app.db.base_model import Base
from app.db.user_model import User
from app.db.address_model import Address
from app.db.user_profile_model import UserProfile

# Import tất cả các model để Base biết
def init_db():
    print("📌 Creating all tables in database...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully.")

if __name__ == "__main__":
    init_db()
