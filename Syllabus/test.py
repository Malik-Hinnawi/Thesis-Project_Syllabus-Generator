from tkinter import filedialog

import PyPDF2
import pandas as pd
from tkinter import *
from tkinter.ttk import *

# Function to extract text from specified page numbers
def extract_text_from_page(pdf_path, page_numbers):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PdfFileReader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize list to store text
        all_text = []

        # Extract text from specified page range
        for page_num in page_numbers:
            page = pdf_reader.pages[page_num - 1]  # Adjust index
            text = page.extract_text()
            all_text.append(text)

        return all_text


# Function to extract document outline
def extract_document_outline(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PdfFileReader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the document outline
        document_outline = pdf_reader.outline

        # Initialize lists to store levels, titles, page numbers, and parent titles
        levels = []
        titles = []
        page_numbers = []
        parent_titles = []

        # Define a recursive function to traverse the document outline
        def traverse_outline(outline_items, level=0, parent_title=None):
            for item in outline_items:
                if isinstance(item, list):
                    # Handle nested outlines
                    traverse_outline(item, level + 1, parent_title)
                elif isinstance(item, dict):
                    # Extract title and page number
                    title = item.get('/Title')
                    page_number = item.get('/Page')

                    if title and page_number:
                        # Append to the lists
                        levels.append(level)
                        titles.append(title)
                        page_numbers.append(pdf_reader.get_page_number(page_number) + 1)  # Adjust index
                        parent_titles.append(parent_title)

                    # Update parent title for child items
                    parent_title = title

        # Start traversing the document outline
        traverse_outline(document_outline)

        # Create a DataFrame from the extracted data
        df = pd.DataFrame({
            'Level': levels,
            'Title': titles,
            'Page Number': page_numbers,
            'Parent Title': parent_titles
        })

        return df


# Create Tkinter GUI
root = Tk()
root.title("PDF Parser")


# Function to handle button click
def parse_pdf():
    # Get user labels
    user_labels = [
        instructor_name_entry.get(),
        course_name_entry.get(),
        office_location_entry.get(),
        office_hours_entry.get(),
        instructor_email_entry.get(),
        phone_number_entry.get()
    ]

    # Prompt user for PDF file path
    pdf_path = filedialog.askopenfilename(title="Select PDF File")

    # Extract text from the first two pages of the PDF
    text = extract_text_from_page(pdf_path, [1, 2])

    # Extract document outline from the PDF
    document_outline_df = extract_document_outline(pdf_path)

    # Print extracted text
    extracted_text.config(state=NORMAL)
    extracted_text.delete('1.0', END)
    for page_num, page_text in enumerate(text, start=1):
        extracted_text.insert(END, f"Page {page_num}:\n{page_text}\n\n")
    extracted_text.config(state=DISABLED)

    # Print document outline DataFrame
    outline_text.config(state=NORMAL)
    outline_text.delete('1.0', END)
    outline_text.insert(END, document_outline_df.to_string(index=False))
    outline_text.config(state=DISABLED)


# Create labels and entry fields for user input
Label(root, text="Instructor Name Label:").grid(row=0, column=0, sticky=W)
instructor_name_entry = Entry(root)
instructor_name_entry.grid(row=0, column=1)

Label(root, text="Course Name Label:").grid(row=1, column=0, sticky=W)
course_name_entry = Entry(root)
course_name_entry.grid(row=1, column=1)

Label(root, text="Office Location Label:").grid(row=2, column=0, sticky=W)
office_location_entry = Entry(root)
office_location_entry.grid(row=2, column=1)

Label(root, text="Office Hours Label:").grid(row=3, column=0, sticky=W)
office_hours_entry = Entry(root)
office_hours_entry.grid(row=3, column=1)

Label(root, text="Instructor Email Label:").grid(row=4, column=0, sticky=W)
instructor_email_entry = Entry(root)
instructor_email_entry.grid(row=4, column=1)

Label(root, text="Phone Number Label:").grid(row=5, column=0, sticky=W)
phone_number_entry = Entry(root)
phone_number_entry.grid(row=5, column=1)

# Button to select PDF file and parse
parse_button = Button(root, text="Parse PDF", command=parse_pdf)
parse_button.grid(row=6, columnspan=2)

# Text widget to display extracted text
Label(root, text="Extracted Text:").grid(row=7, columnspan=2, sticky=W)
extracted_text = Text(root, height=10, width=50, state=DISABLED)
extracted_text.grid(row=8, columnspan=2)

# Text widget to display document outline
Label(root, text="Document Outline:").grid(row=9, columnspan=2, sticky=W)
outline_text = Text(root, height=10, width=50, state=DISABLED)
outline_text.grid(row=10, columnspan=2)

root.mainloop()
