# importing doc to pdf library
from docx2pdf import convert
import os, sys   #need systems file path

def convert_word_to_pdf(input_path, output_path):
    try:
        convert(input_path, output_path)
        print(f'Conversion Completed. PDF saved as {output_path}')
    except Exception as e:
        print(f'An error occured: {str(e)}')


# creating entry point
if __name__== '__main__':
    input_path = r"D:\1. Data Science\10.  Projects\Python Project\Project\abc.docx"
    output_path = r"D:\1. Data Science\10.  Projects\Python Project\Project\output.pdf"

    if os.path.exists(input_path):
        convert_word_to_pdf(input_path, output_path)
    
    else:
        print(f'Input word document file "{input_path}" does not exists..')
