#main.py receives requests and saves data
from fastapi import FastAPI
from backend.models import Expense
from backend.db_models import ExpenseTable
from backend.database import Base
from backend.database import engine
from backend.database import SessionLocal
from fastapi import Depends

app = FastAPI()

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#create route
@app.get("/")
def home():
    return {"Greetings!": "Expense Management API is running"}

#route for /expenses
@app.post("/expenses")
#whatever data comes in, check it using the Expense model
def expenses(expense: Expense, db = Depends(get_db)):
    new_expense = ExpenseTable(
        amount=expense.amount,
        category=expense.category,
        description=expense.description
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

#creates a session and query all the row from table
#and returns all the rows
@app.get("/expenses")
def show_expenses(db = Depends(get_db)):
    expenses = db.query(ExpenseTable).all()
    return expenses

@app.get("/expense_id")
def get_expense_id()