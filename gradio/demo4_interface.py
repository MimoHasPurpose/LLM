import numpy as np
import pandas as pd
import gradio as gr
def reverse_audio(audio):
    sr,data=audio
    reversed_audio=(sr,np.flipud(data))
    return reversed_audio

mic=gr.Audio(sources="microphone",type="numpy",label="Speak heree...... ")
gr.Interface(reverse_audio,mic,"audio").launch()