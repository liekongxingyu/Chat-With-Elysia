import requests
import os
import json

def extract_filename(file_path):
    # 获取文件名（包含后缀）
    file_name_with_extension = os.path.basename(file_path)
    # 分割文件名和后缀
    file_name, file_extension = os.path.splitext(file_name_with_extension)
    # 返回文件名（不包含后缀）
    return file_name


stream_url = 'http://127.0.0.1:5000/tts'
with open('./config.json', 'r', encoding='utf-8') as inform:
    config = json.load(inform)
    ref_audio_path = config['ref_audio_path']


class TextToSpeechPlayer:
    def __init__(self, stream_url, text, character, ref_audio_path):
        self.text = text
        self.character = character
        self.ref_audio_path = ref_audio_path
        self.stream_url = stream_url
        self.payload = {
            "task_type": "text",
            "text": self.text,
            "character": character,
            "emotion": "default",
            "format": "wav",
            "sample_rate": 32000,
            "speed": 1.0,
            "ref_audio_path": self.ref_audio_path,
            "prompt_text": extract_filename(self.ref_audio_path),
        }

    def get_audio_stream(self):
        response = requests.post(
            self.stream_url, json=self.payload, stream=True)
        return response

    def save_audio_file(self, response, output_filename):
        with open(output_filename, 'wb') as f:
            for data in response.iter_content(chunk_size=1024):
                f.write(data)


def generateSound(text, store_path):
    character = "爱莉希雅"
    tts_player = TextToSpeechPlayer(
        stream_url, text, character, ref_audio_path)
    response = tts_player.get_audio_stream()
    output_filename = store_path
    tts_player.save_audio_file(response, output_filename)
