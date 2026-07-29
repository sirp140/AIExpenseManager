#db_models.py describes what the table looks like /defines the database table
#import the SQLAlchamey Base from database file
from backend.database import Base
from sqlalchemy import Column, Integer, Numeric, String

class ExpenseTable(Base):
    __tablename__= "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric(10,2))
    category = Column(String)
    description = Column(String)



