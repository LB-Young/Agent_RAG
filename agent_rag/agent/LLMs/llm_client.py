from openai import OpenAI
from config.config import LLMConfig

class LLMClient:
    def __init__(self):
        self.client.append(OpenAI(api_key=LLMConfig['api_key'], base_url=LLMConfig['base_url']))

    def ado_requests(self, prompt):
        response = self.client.chat.completions.create(
            model=LLMConfig['model'],
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content