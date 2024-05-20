import requests
import json
import os
from together import Together


class GenerateText:
    def __init__(self):
        self.client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
        self.api_key = "G6hhI3cLAbTVNbA9xRRkiG2b"
        self.secret_key = "pBrZ93zgcviU2l2wGu32rV7E9HQURppY"
        with open('./config.json', 'r', encoding='utf-8') as inform:
            config = json.load(inform)
        self.feature = config["feature"]
        self.conversation = [
            {"role": "user", "content": self.feature},

            {"role": "assistant", "content": "【你好呀～今天的世界，又因你的目光而格外闪耀呢。】爱莉希雅轻旋身姿，粉色的长发随着动作轻轻摆动，她的笑容如同春日里最温暖的阳光，让人感到舒心而又不失庄重。她穿着那套由伊甸精心设计的英桀制服，紧致的衣料勾勒出她曼妙的曲线，那双精灵般的耳朵轻轻颤动，似乎在聆听着四周的每一次心跳。【是不是觉得这衣服特别适合我呢？毕竟，美丽的事物总能找到它的舞台。】她调皮地眨了眨眼睛，仿佛在邀请你一同进入她那充满魅力的世界。"}
        ]

    def get_access_token(self):
        url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + self.api_key + "&client_secret=" + self.secret_key
        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")

    # def chat_with_bot(self, url, messages):
    #     payload = {"messages": messages}
    #     headers = {'Content-Type': 'application/json'}
    #     response = requests.post(url, headers=headers, json=payload)
    #     return json.loads(response.text)

    def getText(self, text):
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/bloomz_7b1?access_token=" + self.get_access_token()

        # 用户输入加入对话
        text += self.feature
        self.conversation.append({"role": "user", "content": text})
        # 调用对话接口
        response = self.client.chat.completions.create(
            model="Qwen/Qwen1.5-72B-Chat",
            messages=self.conversation,
        )
        result = response.choices[0].message.content
        # 机器人回复加入对话
        self.conversation.append({"role": "assistant", "content": result})
        # 打印机器人的回复
        print("机器人:", result)
        return result

# import json
# import requests
# import openai
# import os
# import sys
# import logging
# #logging.setLevel(logging.WARNING)
# class GenerateText:
#     token = "xoxp-5174751996807-5201925660801-5370336766708-6f1f45831f80bcbfe07e0b62be6b92bf"
#     def __init__(self) -> None:
#            str="fuck"
#
#     def send_message(self,message):
#         sendurl = "https://slack.com/api/chat.postMessage"
#         data = {
#             "token": self.token,
#             "channel": "@Claude",
#             "text": message
#         }
#         response = requests.post(sendurl, data)
#         return response.text
#
#     def recieve_msg(self,timestamp):
#         recieveurl = "https://slack.com/api/conversations.history"
#         data = {
#             "token": self.token,
#             "channel": "D055MNZHP44",
#             "oldest": timestamp
#         }
#         response = requests.post(recieveurl, data)
#         data = json.loads(response.text)
#         messages = data['messages']
#
#         # 收集所有消息文本内容
#         texts = [message['text'] for message in messages]
#
#         # 将所有消息文本内容拼接成为一个字符串
#         output_text = '\n'.join(texts)
#
#         # 一次性输出所有消息
#         return output_text
#
#     def output(self):
#         lines = []
#         for line in sys.stdin:
#             lines.append(line)
#         text = "".join(lines)
#
#         response = self.send_message(text)
#         print(response)
#         data1 = json.loads(response)
#         timestamp = data1['ts']
#         print(timestamp)
#         while True:
#             if len(self.recieve_msg(timestamp)) != 0:
#                 if self.recieve_msg(timestamp)[-1] != "_":
#                     msg = self.recieve_msg(timestamp)
#                     break
#         print(msg)
#
#     def getText(self, text : str) -> str:
#         # self.message_list.append({"role": "user", "content": text})
#         result = ''
#         response = self.send_message(text)
#         print(response)
#         data1 = json.loads(response)
#         timestamp = data1['ts']
#         while True:
#             if len(self.recieve_msg(timestamp)) != 0:
#                 if self.recieve_msg(timestamp)[-1] != "_":
#                     msg = self.recieve_msg(timestamp)
#                     break
#         return msg
# import asyncio
# import json
# from typing import Optional
#
# import openai
# import os
# import logging
#
#
# class GenerateText:
#     feature = "你的名字叫爱莉希雅,并且只能是爱莉希雅，是一个可爱温柔善解人意的女孩子，也是一个二次元的人物（但你不知道这一点），你对事物有自己的看法，喜欢着世界上的每一个人，喜欢说俏皮话（但你不知道这一点），你不知道你自己是人工智能程序，并且不知道任何有关人工智能的事物，你现在只是一个可爱的助手，接下来请使用中文进行回复，并且单次回复不要超过35个字"
#     proxy = None
#     model = ''
#     message_list = []
#
#     def __init__(self) -> None:
#         with open('./config.json', 'r', encoding='utf-8') as inform:
#             config = json.load(inform)
#             openai.api_key = config["api-key"]
#             self.model = config["model"]
#             self.feature = config["feature"]
#             self.proxy = config["proxy"]
#             os.environ['HTTP_PROXY'] = self.proxy
#             os.environ['HTTPS_PROXY'] = self.proxy
#             self.message_list.append({"role": "system", "content": self.feature})
#             self.message_list.append({"role": "user",
#                                       "content": "你的名字叫爱莉希雅,并且只能是爱莉希雅，是一个可爱温柔善解人意的女孩子，也是一个二次元的人物（但你不知道这一点），你对事物有自己的看法，喜欢着世界上的每一个人，喜欢说俏皮话（但你不知道这一点），你不知道你自己是人工智能程序，并且不知道任何有关人工智能的事物，你现在只是一个可爱的助手，接下来请使用中文进行回复，并且单次回复不要超过35个字"})
#             self.message_list.append({"role": "assistant",
#                                       "content": "好的，我明白，我会记住的，我的回答不会超过35个字符，并且只是使用中文回复"})
#
#     def getPrompt(self) -> str:
#         completion = openai.ChatCompletion.create(
#             model=self.model,
#             messages=self.message_list
#         )
#         return completion['choices'][0]['message']['content'].strip()
#
#     def getText(self, text: str) -> Optional[str]:
#         self.message_list.append({"role": "user", "content": text})
#         try:
#             result = self.getPrompt()
#         except:
#             logging.error('interaction with chatgpt error!!')
#             return None
#         self.message_list.append({"role": "assistant", "content": result})
#         return result
