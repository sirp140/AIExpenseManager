#database.py connects python to SQLite
#import tool to create a connection b/w python & database
from sqlalchemy import create_engine

#tools to create database sessions and database models
from sqlalchemy.orm import sessionmaker, declarative_base

#tells SQLAlchemy to use SQLite and create/use expenses.db
DATABASE_URL = "sqlite:///./expenses.db"

#create the database connection manager
#bridge b/w FastAPI and SQLite
engine = create_engine(
    DATABASE_URL,

    #FastAPI can handle requests using diff. threads
    connect_args={"check_same_thread": False}
)

#Sessions are used to read, add, update or delete data
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#foundation for creating database tables
Base = declarative_base()