from connection import engine
from models import Base

def create_tables():
    print("=" * 60)
    print("Creating Database Tables...")
    print("=" * 60)

    Base.metadata.create_all(bind=engine)

    print("\nAll tables created successfully!")

if __name__ == "__main__":
    create_tables()