import openai
from config import api_key


class MyOpenAI:
    def __init__(self, prompt, model, n, maxtokens, temperature, key):
        self.prompt = prompt
        self.model = model
        self.key = key
        self.n = n
        self.maxtokens = maxtokens
        self.temperature = temperature
        openai.api_key = api_key

    def callgpt(self):
        """
        Calling the GPT API with the Completion module
        Returns a list with all the responses
        """
        response = openai.Completion.create(
            prompt=self.prompt,
            temperature=self.temperature,
            max_tokens=self.maxtokens,
            model=self.model,
            n=self.n,
        )
        resp = []
        for a in range(len(response.choices)):
            resp.append(response.choices[a].text.replace("\n", ""))
        return resp
