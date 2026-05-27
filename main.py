from src.retriever import search_documents


def main():

    query = "What is machine learning?"

    results = search_documents(query)

    print("\nTop Retrieval Results:\n")

    for i, result in enumerate(results, start=1):

        print(f"\nRESULT {i}")
        print(f"Score: {result['score']}")
        print(f"Page: {result['page']}")
        print(f"Type: {result['type']}")

        print(result["text"][:500])


if __name__ == "__main__":
    main()