import os
import shutil
from datetime import datetime
import sys
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

# Directory where Word files are located
source_directory = os.getcwd()
print(source_directory)  # Corrected print statement
# enter the names of the files you want to include
Des = ['','','']

for des in Des:
    # List all Word files containing Des in their name
    word_files = [filename for filename in os.listdir(source_directory) if
                  (des.lower() in filename.lower()) and filename.endswith(".docx")]  # Corrected lowercase comparison
    print(word_files)

    # Sort the files by creation time (most recent first)
    word_files.sort(key=lambda x: datetime.strptime(x.split()[0], '%Y%m%d'), reverse=True)
    print(word_files)

    # Check if there are any matching Word files
    if word_files:
        # Get the most recent Word file
        latest_word_file = word_files[0]

        # Create the destination file name with the current date
        current_date = datetime.now().strftime("%Y%m%d")
        new_file_name = f"{current_date} {des}.docx"

        # Copy the latest Word file to the destination directory
        destination_directory = os.getcwd()
        destination_path = os.path.join(destination_directory, new_file_name)

        # Check if the destination file already exists
        if os.path.exists(destination_path):
            print(f"Error: The file '{new_file_name}' already exists in the destination directory.")
            sys.exit(1)

        # Open the latest Word file using python-docx
        doc = Document(os.path.join(source_directory, latest_word_file))

        # Update the footer with the current date and specific formatting
        for section in doc.sections:
            for footer in section.footer.paragraphs:
                footer.text = f"Last updated {datetime.now().strftime('%B %d, %Y')}"  # Long date format
                run = footer.runs[0]
                run.font.size = Pt(11)
                run.font.name = 'Times New Roman'

        # Save the modified document with the new file name
        doc.save(destination_path)

        print(f"File '{latest_word_file}' copied to '{destination_path}' as '{new_file_name}' with updated footer.")
    else:
        print(f"No Word files containing '{des}' found in the directory.")
