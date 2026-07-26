from fastapi import FastAPI
from backend.models import Expense
app = FastAPI()

#create route
@app.get("/")
def home():
    return {"message": "Expense Management API is running"}

#route for /expenses
@app.post("/expenses")
#whatever data comes in, check it using the Expense model
def expenses(expense: Expense):
    return expense


