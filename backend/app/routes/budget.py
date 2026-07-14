from fastapi import APIRouter
from app.schemas.budget import BudgetCreate, BudgetUpdate
from app.services.budget_service import (
    add_budget,
    get_all_budgets,
    get_budget,
    update_budget,
    delete_budget
)

router = APIRouter(
    prefix="/budget",
    tags=["Budget Management"]
)

@router.post("/create")
def create(budget: BudgetCreate):
    return add_budget(budget)


@router.get("/")
def all_budgets():
    return get_all_budgets()

@router.get("/{budget_id}")
def single_budget(budget_id: str):
    return get_budget(budget_id)

@router.put("/{budget_id}")
def edit_budget(
    budget_id: str,
    budget: BudgetUpdate
):
    return update_budget(
        budget_id,
        budget
    )

@router.delete("/{budget_id}")
def remove_budget(budget_id: str):
    return delete_budget(budget_id)