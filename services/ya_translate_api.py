import requests
from config import FOLDER_ID, TRANSLATE_TOKEN

def get_translation(text: str, target_language: str) -> str:
    body = {
        "targetLanguageCode": target_language,
        "texts": [text],
        "folderId": FOLDER_ID
    }

    headers = {
        "Authorization": f"Bearer {TRANSLATE_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                                 json=body,
                                 headers=headers)
        response.raise_for_status()

        return response.json()["translations"][0]["text"]

    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Непредвиденная ошибка, попробуйте ещё раз"