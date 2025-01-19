import PyPDF2

def reverse_pdf(input_pdf_path, output_pdf_path):
    try:
        print("Starting reverse process...")
        # Open the input PDF file
        with open(input_pdf_path, 'rb') as input_pdf:
            reader = PyPDF2.PdfReader(input_pdf)
            writer = PyPDF2.PdfWriter()

            # Reverse the pages
            for page in reversed(reader.pages):
                writer.add_page(page)

            # Write to the output PDF file
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)

        print(f"Reversed PDF saved as '{output_pdf_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python reverse-pdf-page.py <input_pdf_path> <output_pdf_path>")
    else:
        reverse_pdf(sys.argv[1], sys.argv[2])

