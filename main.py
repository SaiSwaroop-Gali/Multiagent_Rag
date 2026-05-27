from src.parser import extract_pdf_chunks


def main():

    pdf_path = "data/textbook.pdf"

    chunks = extract_pdf_chunks(pdf_path)

    print(f"\nTotal chunks extracted: {len(chunks)}\n")

    print("FIRST CHUNK:\n")

    print(chunks[0])


if __name__ == "__main__":
    main()