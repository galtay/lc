import os
from dotenv import load_dotenv
import openai


load_dotenv(dotenv_path="../dot.env", override=True)
openai.api_key = os.environ["OPENAI_API_KEY"]

# list models
models = openai.Model.list()


# create a chat completion
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}],
)

# print the chat completion
print(chat_completion.choices[0].message.content)
