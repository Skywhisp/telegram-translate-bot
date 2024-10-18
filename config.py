import os

import dotenv

dotenv.load_dotenv('.env')

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

TRANSLATE_TOKEN = os.environ['TRANSLATE_TOKEN']
FOLDER_ID = os.environ['FOLDER_ID']