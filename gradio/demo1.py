import gradio as gr


def greet(name):
    return "Hello " + name
def dance(singer):
    return "you wanna dance with :"+singer

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo2 = gr.Interface(fn=dance, inputs="text", outputs="text")
demo.launch()
demo2.launch()