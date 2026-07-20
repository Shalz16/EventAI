import faiss
import numpy as np


index = None
documents = []


def create_vector_store(embeddings, texts):

    global index
    global documents


    embeddings = np.array(
        embeddings
    ).astype("float32")


    dimension = embeddings.shape[1]


    index = faiss.IndexFlatL2(
        dimension
    )


    index.add(
        embeddings
    )


    documents = texts


    return index



def search_vector(query_embedding, k=3):

    query_embedding = np.array(
        [query_embedding]
    ).astype("float32")


    distances, indices = index.search(
        query_embedding,
        k
    )


    results=[]

    for i in indices[0]:
        results.append(
            documents[i]
        )

    return results