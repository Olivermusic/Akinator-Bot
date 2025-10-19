from json import load
import os
from dotenv import load_dotenv

load_dotenv()

AKI_MONGO_HOST = os.environ.get('aki_mongo_host', "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
BOT_TOKEN = os.environ.get('bot_token', "7968843673:AAEWY9TTBYJR2-1rJmXpFWEyZ4Pkq9LCOSw")
