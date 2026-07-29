#models.py checks incoming data from user/API
from pydantic import BaseModel
class Expense(BaseModel):
    amount: float
    category: str
    description: str
    