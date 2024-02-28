import os
from docx2pdf import convert

def convert_word_to_pdf_in_same_directory():
    current_directory = os.getcwd()

    for filename in os.listdir(current_directory):
        if filename.endswith(".docx"):
            docx_path = os.path.join(current_directory, filename)
            pdf_path = os.path.join(current_directory, os.path.splitext(filename)[0] + ".pdf")

            # Convert .docx to .pdf
            convert(docx_path, pdf_path)

            print(f"Converted {filename} to {os.path.basename(pdf_path)}")

if __name__ == "__main__":
    convert_word_to_pdf_in_same_directory()
