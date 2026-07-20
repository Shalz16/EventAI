from app.rag.embeddings import create_embeddings
from app.rag.vector_store import (
    create_vector_store,
    search_vector
)

from google import genai
from app.config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY
)



def process_documents(chunks):

    embeddings = create_embeddings(chunks)

    create_vector_store(
        embeddings,
        chunks
    )

    return "Knowledge base created"



def ask_question(question):

    # create question embedding
    query_embedding = create_embeddings(
        [question]
    )[0]


    # retrieve relevant documents
    context = search_vector(
        query_embedding
    )


    prompt = f"""
You are an AI Event Management Assistant.

Answer the user question using only the given knowledge.

Knowledge:
{context}


Question:
{question}
"""


    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )


    return response.text