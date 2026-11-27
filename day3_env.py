import os
from dotenv import load_dotenv

load_dotenv()

bot_name = os.getenv("BOT_NAME")

print("Bot Name:", bot_name)
print("Welcome to", bot_name)