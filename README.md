# Video-to-Text 

This is a Python script that translates a video to text. The script uses the `yt_dlp` library to download the video audio, then uses `faster_whisper` model to convert the audio to text. Then uses `gradio` library to show the text in Web UI.

## Usage

To use the script, follow these steps:

1. Install the required libraries in your environment:

```
pip install yt_dlp
pip install faster_whisper
pip install gradio
```

2. Run the script:

```
python video_to_text.py
```

3. Open the browser and go to `http://localhost:7860/`.

4. Enter the URL of the video you want to translate and click on the "Download" button.

5. Wait for the text to be generated and displayed in the output window.

## Example

Here is an example of the script in action:

Hugging face space[https://huggingface.co/spaces/jzyleo/video-to-text]
