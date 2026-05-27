from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


qdrant = QdrantClient(
    url="http://localhost:6333"
)


COLLECTION_NAME = "textbook_content"


def search_documents(query, limit=5):

    query_vector = embedding_model.encode(
        query
    ).tolist()

    results = qdrant.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=limit
    )

    formatted_results = []

    for result in results:

        formatted_results.append({
            "score": result.score,
            "text": result.payload["text"],
            "page": result.payload["page"],
            "type": result.payload["type"]
        })

    return formatted_results