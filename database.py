from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de Railway
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:mWxCGtpzWDLhKGFgbhpeYFtsTkfotabq@crossover.proxy.rlwy.net:40472/turismo_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
