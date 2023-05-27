from myopenai import MyOpenAI
from config import api_key

# Initialization parameters
prompt = "Who was Golda Meir?"
model = "text-davinci-003"
n = 2
maxtokens = 20
temperature = 0.5
key = api_key


# Creating an object and printing to console
my_openai = MyOpenAI(prompt, model, n, maxtokens, temperature, key)
result = my_openai.callgpt()
for response in result:
    print(response + "\n")
