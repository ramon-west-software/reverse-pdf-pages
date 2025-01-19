import os
import PyPDF2

def reverse_pdf(input_pdf_path, output_pdf_path):
    try:
        print(f"Reversing: {input_pdf_path} -> {output_pdf_path}")

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
    # Assuming no arguments provided, process all files in ./pdf-input-directory
    input_dir = './pdf-input-directory'
    output_dir = './pdf-output-directory'
    
    try:
        os.makedirs(output_dir, exist_ok=True)
        for filename in os.listdir(input_dir):
            if filename.endswith('.pdf'):
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)
                reverse_pdf(input_path, output_path)
    except Exception as e:
        print(f"Error processing PDFs: {e}")
