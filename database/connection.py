from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

USERNAME = "Your UserName"
PASSWORD = "Your Password"
HOST = "localhost"
PORT = 3306
DATABASE = "ai_cheque_clearance"

DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DATABASE,
)

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
