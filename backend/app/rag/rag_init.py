import os

from app.rag.document_loader import extract_pdf_text
from app.rag.embeddings import create_embeddings
from app.rag.vector_store import create_vector_store


def initialize_rag():

    folder = os.path.join(
    os.getcwd(),
    "knowledge"
)

    texts = []

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            path = os.path.join(
                folder,
                file
            )

            text = extract_pdf_text(path)

            texts.append(text)


    if not texts:
        print("No documents found")
        return


    embeddings = create_embeddings(
        texts
    )


    create_vector_store(
        embeddings,
        texts
    )


    print("RAG knowledge base loaded successfully")