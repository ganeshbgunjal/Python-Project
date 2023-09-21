import gradio as gr
from utils.convert_helper import convert_word_to_pdf

def gradio_convert_word_to_pdf(input_word): 
    try:
        input_word_path = input_word.name
        output_pdf_path = r"D:\1. Data Science\10.  Projects\Python Project\Project\output2.pdf"

        result_message = convert_word_to_pdf(input_word_path, output_pdf_path)
        return result_message 
    except Exception as e:
        return f"An Error Occured: {str(e)}"
    
# create gradio based interface

demo = gr.Interface(fn=gradio_convert_word_to_pdf,
                    inputs= gr.inputs.File(label= "Input Word Document",type= "file"),
                    outputs= gr.outputs.Textbox(label= "Conversion Status"),
                    live= True,
                    title = "Word To PDF Converter",
                    description = "Convert word document to PDF files",
                       )

if __name__ == "__main__":
    demo.launch()
