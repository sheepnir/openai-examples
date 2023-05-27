"""
Creating chatGPT clone that is calling GPT and Dall-E
"""
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
from config import api_key


app = Flask(__name__)
CORS(app)

openai.api_key = api_key


def my_chat(prompt):
    response = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=100
    )
    return response.choices[0].text


def my_draw(prompt):
    response = openai.Image.create(
        size="256x256", prompt=prompt, n=1, response_format="url"
    )
    return response["data"][0]["url"]


@app.route("/chatbot")
def chatbot():
    pergunta = request.args.get("pergunta")
    if pergunta[0:4] == "img:":
        pergunta = pergunta.replace("img:", "")
        resposta = my_draw(pergunta)
        return jsonify(url_imagem=resposta, resposta="")
    else:
        resposta = my_chat(pergunta)
        return jsonify(resposta=resposta)


"""
Test with the following code:
import requests
x = requests.get(http://127.0.0.1:5000/chatbot?pergunta=who is golda meir?)
print(x.text)
"""

app.run()
