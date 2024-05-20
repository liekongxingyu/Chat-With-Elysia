import json
import os
from together import Together


class GenerateText:
    def __init__(self):
        self.client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
        with open('./config.json', 'r', encoding='utf-8') as inform:
            config = json.load(inform)
        self.feature = config["feature"]
        self.firstReply = config['firstReply']
        self.model = config['model']
        self.conversation = [
            {"role": "user", "content": self.feature},
            {"role": "assistant", "content": self.firstReply}
        ]

    def getText(self, text):
        # 用户输入加入对话
        text += self.feature
        self.conversation.append({"role": "user", "content": text})
        # 调用对话接口
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation,
        )
        result = response.choices[0].message.content
        # 机器人回复加入对话
        self.conversation.append({"role": "assistant", "content": result})
        # 打印机器人的回复
        print("机器人:", result)
        return result
