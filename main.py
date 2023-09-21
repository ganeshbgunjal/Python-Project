from utils.helper import WordToPDFConverter
import os

class WordToPDFApp:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        
    def Convert(self):
        if __name__== '__main__':
            if os.path.exists(self.input_path):
                WordToPDFConverter.convert_word_to_pdf(self.input_path, self.output_path)
            else:
                print(f'Input word document file "{self.input_path}" does not exists..')

if __name__== '__main__':
    input_path = r"D:\1. Data Science\10.  Projects\Python Project\Project\abc.docx"
    output_path = r"D:\1. Data Science\10.  Projects\Python Project\Project\output1.pdf"

    app = WordToPDFApp(input_path, output_path)

    app.Convert()
    