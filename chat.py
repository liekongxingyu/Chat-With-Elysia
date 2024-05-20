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
