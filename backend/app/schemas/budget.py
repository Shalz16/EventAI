from pydantic import BaseModel

class BudgetCreate(BaseModel):
    event_id: str
    total_budget: float
    food_cost: float
    decoration_cost: float
    equipment_cost: float
    miscellaneous_cost: float


class BudgetUpdate(BaseModel):
    total_budget: float
    food_cost: float
    decoration_cost: float
    equipment_cost: float
    miscellaneous_cost: float