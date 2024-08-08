import os

from dotenv import load_dotenv

load_dotenv(
    "config.env" if os.path.isfile("config.env") else "sample_config.env"
)

BOT_TOKEN = "5221050210:AAHmrX6Vx1ebc36QJ5xGBpJMCdd9LlfnlA8"
API_ID = int(os.environ.get("API_ID"))
SESSION_STRING = os.environ.get("SESSION_STRING", "BQFYqSoAxWtU5iS1U7ZlW_dC4YY5PgJsV9lqxIGSvyBH1KzzDiwS9M1OqpMC8VquOLLdvDauOCVzmE6eto_sZwZAcBA9iG5nhkFlqgfGUX5jTJ2DduICJ1_ivSw1Fq69QeYn5n1DFD5L_nlkK_i1IrDcgoLomBVtwpnfb2RgnILLe8JCHYDrmlxRxv5CjHj6naL1_Wf7-b0DqCHxVsuHfSQJyBFBSqYVK47zvSHVHUIBHpWu7hVbVwlKrMAG65xV-5UV1JNy31Vja5z_NZIkyQwRZVdBdZyTZMuCcfDL-DRB-6HR5IajdZvzpaJXOsrJ0uPibiVoAoiBQewmdni3FNl1G5NrlAAAAAGkdF1FAA")
API_HASH = os.environ.get("API_HASH")
USERBOT_PREFIX = os.environ.get("USERBOT_PREFIX", ".")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
SUDO_USERS_ID = list(map(int, os.environ.get("SUDO_USERS_ID", "").split()))
LOG_GROUP_ID = int(os.environ.get("LOG_GROUP_ID"))
GBAN_LOG_GROUP_ID = int(os.environ.get("GBAN_LOG_GROUP_ID"))
MESSAGE_DUMP_CHAT = int(os.environ.get("MESSAGE_DUMP_CHAT"))
WELCOME_DELAY_KICK_SEC = int(os.environ.get("WELCOME_DELAY_KICK_SEC", 600))
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://aashish:aashish@jdmv.4f6gh.mongodb.net/?retryWrites=true&w=majority&appName=jdmv")
ARQ_API_KEY = os.environ.get("ARQ_API_KEY")
ARQ_API_URL = os.environ.get("ARQ_API_URL", "https://arq.hamker.dev")
LOG_MENTIONS = os.environ.get("LOG_MENTIONS", "True").lower() in ["true", "1"]
RSS_DELAY = int(os.environ.get("RSS_DELAY", 300))
PM_PERMIT = os.environ.get("PM_PERMIT", "True").lower() in ["true", "1"]
