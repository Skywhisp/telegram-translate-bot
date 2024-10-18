# Telegram бот для перевода текста

Этот проект представляет собой Telegram-бота, 
который позволяет пользователям переводить слова между различными языками 
с помощью Yandex Translate API. 

[Документация Yandex Translate API](https://yandex.cloud/ru/docs/translate/)

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone <URL_репозитория>
   cd <имя_папки_репозитория>
   ```
2. **Создайте виртуальное окружение и активируйте его:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows используйте venv\Scripts\activate
   ```
3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt # На Windows используйте py -m pip install -r requirements.txt 
   ```
4. **Создайте файл .env в корне проекта и добавьте ваши токены:**

   ```plaintext
   TELEGRAM_TOKEN=ваш_токен_телеграм
   TRANSLATE_TOKEN=ваш_токен_перевода
   FOLDER_ID=ваш_id_папки
   ```
