from simplechatgpt import Chat
import os

key = os.environ["OPENAI_API_KEY"]
chat = Chat(key)

print(chat.send("Hello, how are you?"))
