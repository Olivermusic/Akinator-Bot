from json import load
import os
from dotenv import load_dotenv

load_dotenv()

AKI_MONGO_HOST = os.environ.get('aki_mongo_host', "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
BOT_TOKEN = os.environ.get('bot_token', "5871718163:AAEKVvHBTTYURGJsBEIpcCiSx0c1bNAk2PY")
