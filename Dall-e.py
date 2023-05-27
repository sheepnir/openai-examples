import openai
from config import api_key
import shutil
import requests


openai.api_key = api_key

response = openai.Image.create(
    prompt="Create a classic oil painting image of Golda Meir",
    size="256x256",  # 512x512   #1024x1024
    n=1,
    response_format="url",
)
image_url = response["data"][0]["url"]
print(response["data"][0]["url"])


def save_image(image_url, file_name):
    # Saving the generated image to a file
    image_res = requests.get(image_url, stream=True)

    if image_res.status_code == 200:
        with open(file_name, "wb") as f:
            shutil.copyfileobj(image_res.raw, f)
            print("Image downloaded successfully")
    else:
        print("Image downloading failed")
    return image_res.status_code


save_image(image_url, file_name="imageX.png")
