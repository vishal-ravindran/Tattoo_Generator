# Source code for accessing DALL-E in Open AI

from openai import OpenAI
from decouple import config

OPEN_API_KEY = config('OPEN_API_KEY')

client = OpenAI(api_key=OPEN_API_KEY)


# def generate_tattoo(prompt="Generate a tattoo of persian cat", n=3):
def generate_tattoo(prompt="", n=3):
    num = int(n)

    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="256x256",
        quality="standard",
        n=num,
    )
    print(response)
    URL_list = []
    for i in range(num):
        URL_list.append(response.data[i].url)

    # image_url = response.data[0].url
    print("\n\n[INSIDE generate_tattoo function]", URL_list)

    return URL_list
