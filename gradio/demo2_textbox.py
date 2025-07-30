import gradio as gr

def greet(name):
    return "Hello : "+name

textbox=gr.Textbox(label="enter ya name: ",placeholder="John doe",lines=2)
gr.Interface(fn=greet,inputs=textbox,outputs="text").launch()