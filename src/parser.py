import fitz


def extract_pdf_chunks(pdf_path: str):
    doc = fitz.open(pdf_path)

    chunks = []

    for page_num, page in enumerate(doc):

        blocks = page.get_text("blocks")

        for block in blocks:

            text = block[4].strip() if len(block) > 4 else ""

            if len(text) < 80:
                continue

            cleaned_text = " ".join(text.split())

            chunk = {
                "text": cleaned_text,
                "metadata": {
                    "page": page_num + 1,
                    "source": pdf_path,
                    "type": "text"
                }
            }

            chunks.append(chunk)

    return chunks