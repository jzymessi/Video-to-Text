import gradio as gr
import yt_dlp
import os

from faster_whisper import WhisperModel
# tiny, tiny.en, base, base.en, small, small.en, medium, medium.en, large-v1, large-v2, large-v3, or large
model_name = 'base'
model = WhisperModel(model_name, device="cuda", download_root="./models",local_files_only=True)

ydl_opts = {
    'outtmpl': 'demo.m4a',
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }],
    'proxy': 'socks5://192.168.2.18:20170',
}

def download_audio(url):
    if os.path.exists('demo.m4a'):
        os.remove('demo.m4a')
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        code = ydl.download([url])
    assert code == 0, "Failed to download audio"

    segments, info = model.transcribe("demo.m4a", beam_size=5)
    print("Transcript:", info.language)
    partial_message = "" 
    for segment in segments:
        msg = "[%.2fs -> %.2fs] %s\n" % (segment.start, segment.end, segment.text)
        partial_message += msg
        yield partial_message

with gr.Blocks() as demo:
    with gr.Column():
        name = gr.Textbox(label="Enter your video url")
        button = gr.Button("Download")

    with gr.Column():
        output = gr.TextArea(label="Output")

    button.click(
        download_audio,
        inputs=[name],
        outputs=[output],
    )


demo.launch(server_name="0.0.0.0")