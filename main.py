import os
import openai
from instance.config import API_KEY

from dotenv import load_dotenv



load_dotenv()
os.environ["API_KEY"] = os.getenv("API_KEY", API_KEY)
openai.api_key = API_KEY


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        message =[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()



if __name__ == "__main__":
    while True:
        user_input = input("You:")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("ChatBot: ", response)