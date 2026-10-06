import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city):
    """
    Şehir adından enlem, boylam ve ülke bilgisini bulur.
    """

    params = {
        "name": city,
        "count": 1,
        "language": "tr",
        "format": "json"
    }

    response = requests.get(GEOCODING_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        return None

    location = data["results"][0]

    return {
        "name": location.get("name"),
        "country": location.get("country"),
        "latitude": location.get("latitude"),
        "longitude": location.get("longitude")
    }


def get_weather(city):
    """
    Verilen şehir için güncel hava durumu ve saatlik tahminleri getirir.
    """

    location = get_coordinates(city)

    if not location:
        return None

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "is_day,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m,"
            "visibility"
        ),
        "hourly": (
            "temperature_2m,"
            "precipitation_probability,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m"
        ),
        "forecast_days": 7,
        "timezone": "auto"
    }

    response = requests.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    return {
        "location": location,
        "current": data.get("current", {}),
        "hourly": data.get("hourly", {}),
        "timezone": data.get("timezone")
    }

def weather_code_to_text(code):
    """Open-Meteo hava durumu kodunu Türkçe açıklamaya çevirir."""

    weather_codes = {
        0: "Açık",
        1: "Çoğunlukla açık",
        2: "Parçalı bulutlu",
        3: "Kapalı",
        45: "Sisli",
        48: "Kırağılı sis",
        51: "Hafif çisenti",
        53: "Çisenti",
        55: "Yoğun çisenti",
        56: "Hafif donan çisenti",
        57: "Yoğun donan çisenti",
        61: "Hafif yağmur",
        63: "Yağmur",
        65: "Kuvvetli yağmur",
        66: "Hafif donan yağmur",
        67: "Kuvvetli donan yağmur",
        71: "Hafif kar",
        73: "Kar",
        75: "Yoğun kar",
        77: "Kar taneleri",
        80: "Hafif sağanak",
        81: "Sağanak",
        82: "Kuvvetli sağanak",
        85: "Hafif kar sağanağı",
        86: "Kuvvetli kar sağanağı",
        95: "Gök gürültülü fırtına",
        96: "Dolu ihtimalli gök gürültülü fırtına",
        99: "Kuvvetli dolu ihtimalli fırtına"
    }

    try:
        code = int(code)
    except (TypeError, ValueError):
        return "Bilinmeyen hava durumu"

    return weather_codes.get(
        code,
        "Bilinmeyen hava durumu"
    )