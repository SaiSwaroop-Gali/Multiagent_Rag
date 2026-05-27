from dotenv import load_dotenv

from src.parser import extract_pdf_chunks
from src.database import create_vector_store


load_dotenv()


def main():

    pdf_path = "data/textbook.pdf"

    chunks = extract_pdf_chunks(pdf_path)

    print(f"\nExtracted {len(chunks)} chunks")

    print("\nGenerating embeddings and storing vectors...")

    qdrant = create_vector_store(chunks)

    print("\nVector database successfully created!")

    print(qdrant.get_collections())


if __name__ == "__main__":
    main()