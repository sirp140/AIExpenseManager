from fastapi import FastAPI
app = FastAPI()

#create route
@app.get("/")
def home():
    return {"message": "Expense Management API is running"}

