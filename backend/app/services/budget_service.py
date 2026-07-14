from bson import ObjectId
from app.database import db
from app.models.budget import create_budget


def add_budget(budget):
    budgets = db.budgets

    new_budget = create_budget(budget)

    result = budgets.insert_one(new_budget)

    return {
        "message": "Budget Created Successfully",
        "budget_id": str(result.inserted_id)
    }


def get_all_budgets():
    budgets = db.budgets.find()

    data = []

    for budget in budgets:
        budget["_id"] = str(budget["_id"])
        data.append(budget)

    return data

def get_budget(budget_id):
    budgets = db.budgets

    budget = budgets.find_one(
        {"_id": ObjectId(budget_id)}
    )

    if not budget:
        return {"message": "Budget not found"}

    budget["_id"] = str(budget["_id"])

    return budget

def update_budget(budget_id, budget):
    budgets = db.budgets

    result = budgets.update_one(
        {"_id": ObjectId(budget_id)},
        {
            "$set": {
                "total_budget": budget.total_budget,
                "food_cost": budget.food_cost,
                "decoration_cost": budget.decoration_cost,
                "equipment_cost": budget.equipment_cost,
                "miscellaneous_cost": budget.miscellaneous_cost
            }
        }
    )

    if result.modified_count == 0:
        return {"message": "Budget not found or no changes made"}

    return {"message": "Budget Updated Successfully"}

def delete_budget(budget_id):
    budgets = db.budgets

    result = budgets.delete_one(
        {"_id": ObjectId(budget_id)}
    )

    if result.deleted_count == 0:
        return {"message": "Budget not found"}

    return {"message": "Budget Deleted Successfully"}