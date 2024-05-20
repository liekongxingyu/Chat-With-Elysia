import gradio as gr
import webbrowser
from parse import Parse
import torch
if __name__ == '__main__':
    ps = Parse()
    print(torch.__version__)
    with gr.Blocks() as app:
        gr.Markdown(
            "# <center> Chat with Elysia\n"
            "### <center> base on chat TogetherAI and GSVI\n"
        )
        
        with gr.Row():
            with gr.Column():
                textbox = gr.TextArea(label="对话内容",
                                        placeholder="Type your sentence here",
                                        value="你好", elem_id=f"tts-input")
            with gr.Column():
                text_output = gr.Textbox(label="回复信息")
                audio_output = gr.Audio(label="音频信息", elem_id="tts-audio")
                btn = gr.Button("生成对话")
                btn.click(ps.PipeChat,
                            inputs=[textbox],
                            outputs=[text_output, audio_output])
    webbrowser.open("http://127.0.0.1:7860")
    app.launch()