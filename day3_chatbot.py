import json
import os
from dotenv import load_dotenv

load_dotenv()
BOT_NAME = os.getenv("BOT_NAME", "KaviyaBot")


class ChatBot:

    def __init__(self, name):
        self.name = name
        self.history = []

    def add_message(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

    def get_reply(self, message):
        replies = {
            "hello": "Hello! How are you?",
            "hi": "Hi! Welcome!",
            "python": "Python is a programming language.",
            "bye": "Goodbye!"
        }

        message = message.lower().strip()

        for keyword, reply in replies.items():
            if keyword in message:
                return reply

        return "Sorry, I don't understand."

    def save_history(self):
        with open("chat_history.json", "w") as file:
            json.dump(self.history, file, indent=4)

    def load_history(self):
        try:
            with open("chat_history.json", "r") as file:
                self.history = json.load(file)
        except FileNotFoundError:
            print("No previous history found.")


bot = ChatBot(BOT_NAME)
bot.load_history()

print("Welcome to", bot.name)
print("Type 'bye' to exit.")

while True:

    user_message = input("You: ")

    bot.add_message("user", user_message)

    reply = bot.get_reply(user_message)

    print("Bot:", reply)

    bot.add_message("bot", reply)

    if user_message.lower().strip() == "bye":
        break

bot.save_history()

print("Chat history saved!")