from datetime import datetime

def create_budget(budget):
    return {
        "event_id": budget.event_id,
        "total_budget": budget.total_budget,
        "food_cost": budget.food_cost,
        "decoration_cost": budget.decoration_cost,
        "equipment_cost": budget.equipment_cost,
        "miscellaneous_cost": budget.miscellaneous_cost,
        "created_at": datetime.utcnow()
    }