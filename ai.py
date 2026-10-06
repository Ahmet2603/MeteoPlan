import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


load_dotenv()


try:
    API_KEY = st.secrets.get(
        "GEMINI_API_KEY",
        os.getenv("GEMINI_API_KEY")
    )
except Exception:
    API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY bulunamadı. "
        "Streamlit Secrets veya .env dosyanızı kontrol edin."
    )


client = genai.Client(api_key=API_KEY)


def generate_daily_plan(
    city,
    temperature,
    description,
    humidity,
    wind_speed
):
    prompt = f"""
Sen MeteoPlan adlı hava durumuna göre günlük plan
önerileri oluşturan bir yapay zekâ asistanısın.

Şehir: {city}
Sıcaklık: {temperature} °C
Hava durumu: {description}
Nem: %{humidity}
Rüzgâr: {wind_speed} km/sa

Bu hava koşullarına göre kullanıcı için pratik
ve anlaşılır bir günlük plan öner.

Önerilerini saatlere göre sırala.
Dışarıda yapılabilecek aktiviteler ile
içeride yapılabilecek aktiviteleri dengeli şekilde belirt.

Yanıtı Türkçe ver.
Kısa, anlaşılır ve günlük hayatta uygulanabilir olsun.
"""

    models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite"
    ]

    last_error = None

    for model in models:
        try:
            chat = client.chats.create(model=model)

            response = chat.send_message(prompt)

            return response.text

        except Exception as error:
            last_error = error

            if "503" in str(error):
                continue

            raise error

    raise last_error

