from fastapi import FastAPI
from backend.models import Expense
app = FastAPI()

expense_list = []

#create route
@app.get("/")
def home():
    return {"Greetings!": "Expense Management API is running"}

#route for /expenses
@app.post("/expenses")
#whatever data comes in, check it using the Expense model
def expenses(expense: Expense):
    expense_list.append(expense)
    return expense_list

@app.get("/expenses")
def show_expenses():
    return expense_list

    


