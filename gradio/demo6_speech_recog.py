from transformers import pipeline
import gradio as gr

models = pipeline("automatic-speech-recognition",model="stevhliu/my_awesome_asr_mind_model")


def transcribe_audio(audio):
    transcription = models(audio)["text"]
    return transcription


gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
).launch()