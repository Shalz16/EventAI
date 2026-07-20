from fastapi import APIRouter
from app.rag.rag_service import ask_question


router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@router.post("/ask")
def ask(data:dict):

    question=data["question"]

    answer=ask_question(
        question
    )


    return {
        "result":answer
    }