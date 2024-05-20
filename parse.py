import os
import sys
import datetime
import json
from soundMaker import *
from chat import GenerateText
import logging


class Parse:
    role_name = ''
    gt = None
    store_path = ''
    begin_time = ''
    file_name = ''
    cnt = 0

    def __init__(self) -> None:
        with open('./config.json', 'r', encoding='utf-8') as inform:
            config = json.load(inform)
            self.role_name = config["name"]
            self.store_path = config["store-path"]
        self.gt = GenerateText()
        date = datetime.datetime.now()
        self.file_name = date.strftime('%Y-%m-%d-%H-%M-%S')
        self.store_path = self.store_path + '/' + self.file_name
        os.mkdir(self.store_path)

    def getText(self, text):
        result = ''
        with open(self.store_path + '/content.txt', 'a', encoding='utf-8') as cntt:
            cntt.write('user: ' + text + '\n')
            result = self.gt.getText(text)
            if result is None:
                sys.exit()
            cntt.write(self.role_name + ': ' + result +
                       '--------------------------------------\n')
        return result

    def switchAudio(self, text):
        audio_path = self.store_path + '/' + str(self.cnt) + '.wav'
        self.cnt += 1
        generateSound(text, audio_path)
        logging.warning('text change to audio successfully!')
        return text, audio_path

    def PipeChat(self, text):
        return self.switchAudio(self.getText(text))



