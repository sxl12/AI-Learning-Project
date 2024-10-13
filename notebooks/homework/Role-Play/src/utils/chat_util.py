from .meta_info import MetaData
from utils import  ConfigLoader

from zhipuai import ZhipuAI
import os

class ChatUtils:
    def __init__(self):
        self.client = ZhipuAI(api_key=os.getenv("ZHIPU_API_KEY"))
        self.model = "charglm-3"

    def get_info(self):
        meta = MetaData()
        configloader = ConfigLoader()
        config = configloader.load_config()
        system_prompt = config['system_prompt']
        iteration_num = config['iteration_num']
        

        li_name = config['li']['name']
        li_description = config['li']['description']
        start_message = config['start_message']

        li_meta_data = meta.get_meta(li_description,li_name)
        li_history = [
             {
                "role": "assistant",
                "content": system_prompt 
            }
        ]

        ye_name = config['ye']['name']
        ye_description = config['ye']['description']
        ye_meta_data = meta.get_meta(ye_description, ye_name)
        ye_history = [
             {
                "role": "assistant",
                "content": system_prompt 
            }
        ]
        return li_meta_data, li_history, ye_meta_data, ye_history,start_message,iteration_num

    
    def start_chat(self,meta,history):
        try:
            response = self.client.chat.completions.create(
                model=self.model,  # 填写需要调用的模型名称
                meta= meta,
                messages=history,
                stream=True
            )
        except Exception as e:
            print(f"meta: {meta}, history: {history}")
            print(e)
        content = ''
        for chunk in response:
            content += chunk.choices[0].delta.content

        return content
        
        
