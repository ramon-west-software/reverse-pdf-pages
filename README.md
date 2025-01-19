# Reverse PDF Tool

## Overview
This Python script reverses the page order of PDF files. It reads PDF files from a designated input directory, reverses the order of their pages, and saves the output in a specified output directory.

## Features
- Reads all PDF files from the `./pdf-input-directory`.
- Reverses the page order of each PDF file.
- Saves the reversed PDF files to the `./pdf-output-directory`.
- Automatically creates the output directory if it does not exist.

## Prerequisites
### Python Version
- Python 3.6 or higher.

### Required Libraries
- `PyPDF2`

Install the required library by running:
```bash
pip install PyPDF2
```

## How to Use
1. Place your PDF files in the `./pdf-input-directory`.
2. Run the script using:
   ```bash
   python reverse_pdf.py
   ```
3. The reversed PDFs will be saved in the `./pdf-output-directory`.

## Directory Structure
Ensure the following directory structure exists or will be created:
```
./
|-- pdf-input-directory/      # Input directory containing PDF files
|-- pdf-output-directory/     # Output directory for reversed PDF files
|-- reverse_pdf.py            # Script file
```

## Code Explanation
- **reverse_pdf(input_pdf_path, output_pdf_path):**
  - Accepts input and output PDF file paths.
  - Opens the input PDF, reverses its pages, and writes the reversed content to the output file.

- **Main Execution Block:**
  - Processes all `.pdf` files in `./pdf-input-directory`.
  - Creates the `./pdf-output-directory` if it does not exist.
  - Calls the `reverse_pdf` function for each file.

## Error Handling
- Captures and logs any exceptions during the file processing.
- Handles directory creation failures or issues with reading/writing PDF files.

## Example
1. Place `example.pdf` in the `./pdf-input-directory`.
2. Run the script.
3. The reversed version of `example.pdf` will be available in `./pdf-output-directory`.

## Notes
- Ensure that the input PDFs are not corrupted and are properly formatted.
- Test the script on a sample PDF before using it on critical documents.

## License
This project is licensed under the MIT License. Feel free to use and modify the script as needed.

