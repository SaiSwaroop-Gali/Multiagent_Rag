from dotenv import load_dotenv
from pathlib import Path


env_path = Path(".") / ".env"

load_dotenv(dotenv_path=env_path)

from src.retriever import search_documents
from src.generator import generate_answer


def main():

    query = "What is machine learning?"

    results = search_documents(
        query=query,
        limit=5
    )

    contexts = [
        result["text"]
        for result in results
    ]

    answer = generate_answer(
        query=query,
        contexts=contexts
    )

    print("\nGENERATED ANSWER:\n")

    print(answer)

    print("\nSOURCES:\n")

    for i, result in enumerate(results, start=1):

        print(f"\nSOURCE {i}")

        print(f"Page: {result['page']}")

        print(f"Score: {result['score']}")

        print(result["text"][:300])


if __name__ == "__main__":
    main()