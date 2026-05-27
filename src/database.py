import uuid

from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


def create_vector_store(chunks):

    embedding_model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    qdrant = QdrantClient(
        url="http://localhost:6333"
    )

    collection_name = "textbook_content"

    existing_collections = [
        c.name for c in qdrant.get_collections().collections
    ]

    # Create collection only if it does not exist
    if collection_name not in existing_collections:

        qdrant.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

    points = []

    for chunk in chunks:

        embedding = embedding_model.encode(
            chunk["text"]
        ).tolist()

        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding,
            payload={
                "text": chunk["text"],
                **chunk["metadata"]
            }
        )

        points.append(point)

    qdrant.upsert(
        collection_name=collection_name,
        points=points
    )

    return qdrant