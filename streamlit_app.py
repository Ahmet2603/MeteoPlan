import streamlit as st
st.set_page_config(
    page_title="MeteoPlan",
    page_icon="🌤️",
    layout="wide"
)
# -------------------------------------------------
# MODERN METEOPLAN TASARIMI
# -------------------------------------------------

st.markdown("""
<style>

[data-testid="stHeader"] {
    background: transparent !important;
}

/* Saatlik hava kartları */

.hourly-scroll {
    display: flex;
    gap: 10px;

    overflow: hidden;

    padding: 8px 4px 14px 4px;
    margin-top: 10px;

    width: 100%;
}

.hourly-card {
    min-width: calc((100% - 50px) / 6);
    max-width: calc((100% - 50px) / 6);

    background: linear-gradient(
        145deg,
        #182b50,
        #10203f
    );

    border: 1px solid #28518d;
    border-radius: 12px;

    padding: 10px 8px;

    text-align: center;

    box-shadow:
        0 6px 16px rgba(0, 0, 0, 0.22);

    flex-shrink: 0;
}

.hourly-time {
    color: #f8fafc !important;
    font-size: 15px;
    font-weight: 700;
}

.hourly-icon {
    font-size: 30px;
    margin: 12px 0;
}

.hourly-temperature {
    color: #f8fafc !important;
    font-size: 20px;
    font-weight: 700;
}

.hourly-weather {
    color: #94a3c7 !important;
    font-size: 12px;
    margin-top: 5px;
}

.hourly-rain {
    color: #60a5fa !important;
    font-size: 12px;
    margin-top: 10px;
}

/* Hava durumu geçmişi */

.history-card {
    background: linear-gradient(
        145deg,
        #182442,
        #111a31
    );
    border: 1px solid #29395f;
    border-radius: 18px;
    padding: 18px;
    margin-top: 12px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);

    max-height: 320px;
    overflow: auto;
    resize: vertical;
}

.history-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}

.history-table th {
    color: #94a3c7 !important;
    font-size: 13px;
    font-weight: 600;
    text-align: left;
    padding: 12px 10px;
    border-bottom: 1px solid #29395f;
}

.history-table td {
    color: #e2e8f0 !important;
    font-size: 14px;
    padding: 12px 10px;
    border-bottom: 1px solid rgba(41, 57, 95, 0.5);
}

.history-table tr:last-child td {
    border-bottom: none;
}

.history-table tr:hover {
    background: rgba(96, 165, 250, 0.06);
}
    /* Bölüm başlıkları */
    .section-title {
        font-size: 24px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }
   
    /* Favori şehir kartları */

.favorite-city-card {
    background: linear-gradient(
        145deg,
        #1b3154,
        #142746
    );
    border: 1px solid #29395f;
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 8px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    transition: 0.2s ease;
}

.favorite-city-card:hover {
    transform: translateY(-3px);
    border-color: #60a5fa;
}

.favorite-city-icon {
    font-size: 28px;
    margin-bottom: 8px;
}

.favorite-city-name {
    color: #f8fafc !important;
    font-size: 17px;
    font-weight: 700;
}
/* =================================================
   METEOPLAN YENİ MODERN TASARIM
   ================================================= */

.block-container {
    max-width: 1450px !important;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
}

.stApp {
    background: #071329 !important;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(
            circle at 10% 5%,
            rgba(40, 80, 180, 0.18),
            transparent 35%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(80, 40, 180, 0.12),
            transparent 30%
        ),
        #071329 !important;
}

/* Ana başlık */
h1 {
    font-size: 42px !important;
    font-weight: 800 !important;
    color: #f8fafc !important;
    letter-spacing: -1px;
}

/* Alt başlıklar */
h2, h3, h4 {
    color: #f8fafc !important;
    font-weight: 700 !important;
}

/* Normal yazılar */
p {
    color: #cbd5e1 !important;
}

/* Butonlar */
.stButton > button {
    border-radius: 12px !important;
    min-height: 44px !important;
    font-weight: 600 !important;
    border: 1px solid #244a91 !important;
    background: #0d1b38 !important;
    color: #e2e8f0 !important;
    transition: 0.2s ease !important;
}

.stButton > button:hover {
    border-color: #60a5fa !important;
    transform: translateY(-2px);
}

/* =================================================
   METEOPLAN HEDEF TASARIM - ANA HAVA KARTI
   ================================================= */

.weather-info-card {
    background: linear-gradient(
        135deg,
        #09295f 0%,
        #071b42 100%
    ) !important;

    border: 1px solid #087cff !important;
    border-radius: 16px !important;

    padding: 20px 22px !important;
    min-height: 135px !important;

    box-shadow:
        0 0 20px rgba(0, 124, 255, 0.18),
        inset 0 0 25px rgba(15, 75, 160, 0.10) !important;

    transition: all 0.2s ease !important;
}

.weather-info-card:hover {
    transform: translateY(-2px) !important;

    box-shadow:
        0 0 28px rgba(0, 124, 255, 0.25),
        inset 0 0 25px rgba(15, 75, 160, 0.15) !important;
}
/* Saatlik kartlar */
.hourly-card {
    background: linear-gradient(
        145deg,
        #10244b,
        #0b1936
    ) !important;
    border: 1px solid #1d4382 !important;
    border-radius: 16px !important;
    box-shadow: 0 8px 22px rgba(0, 0, 0, 0.25) !important;
    transition: 0.2s ease !important;
}

.hourly-card:hover {
    transform: translateY(-4px);
    border-color: #4f8cff !important;
}

/* Favori şehir */
.favorite-city-card {
    background: linear-gradient(
        145deg,
        #10244b,
        #0b1936
    ) !important;
    border: 1px solid #1e4b91 !important;
    border-radius: 16px !important;
}

/* AI kartı */
.ai-plan-card {
    background: linear-gradient(
        145deg,
        #121f4a,
        #0b1735
    ) !important;
    border: 1px solid #4c3f9e !important;
    border-radius: 18px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25) !important;
}

/* Kayıtlı notlar */
.saved-notes-card,
.saved-note-item {
    background: linear-gradient(
        145deg,
        #10244b,
        #0b1936
    ) !important;
    border-color: #1e4b91 !important;
}

/* Form */
.stForm {
    background: linear-gradient(
        145deg,
        #0d1d3b,
        #0a1730
    ) !important;
    border: 1px solid #243d6d !important;
    border-radius: 18px !important;
    padding: 18px !important;
}

/* Ayırıcı çizgiler */
hr {
    border-color: #1c3157 !important;
}

/* Saatlik grafik alanı */
[data-testid="stArrowVegaLiteChart"],
[data-testid="stLineChart"] {
    background: #09152c !important;
    border-radius: 18px !important;
}
/* =================================================
   METEOPLAN ÜST BAŞLIK
   ================================================= */

.meteo-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 18px;
    padding-top: 4px;
}

.meteo-logo {
    font-size: 52px;
    line-height: 1;
    filter: drop-shadow(0 4px 10px rgba(79, 140, 255, 0.18));
}

.meteo-brand {
    color: #f8fafc;
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1.05;
}

.meteo-subtitle {
    color: #8fa4c7;
    font-size: 13px;
    margin-top: 5px;
    line-height: 1.3;
}

.meteo-header .meteo-subtitle {
    color: #94a3c7 !important;
    font-size: 13px;
    margin-top: 3px;
}

/* =================================================
   ANA HAVA DURUMU KARTI - HEDEF TASARIM
   ================================================= */

.main-weather-card {
    display: grid;
    grid-template-columns: 40% 1px 60%;
    align-items: center;

    background: linear-gradient(
        145deg,
        #102a55,
        #0b1b3a
    );

    border: 1px solid #1769d1;
    border-radius: 18px;

    padding: 20px 22px;
    margin-top: 14px;

    min-height: 155px;

    box-shadow:
        0 12px 30px rgba(0, 0, 0, 0.28);
}


/* SOL TARAF */

.main-weather-left {
    display: flex;
    align-items: center;
    gap: 16px;
}

.main-weather-icon {
    font-size: 58px;
    line-height: 1;
}

.main-temperature {
    color: #f8fafc;
    font-size: 38px;
    font-weight: 800;
    line-height: 1.05;
}

.main-weather-description {
    color: #9bb0d0;
    font-size: 14px;
    margin-top: 7px;
}


/* ORTA AYIRICI */

.main-weather-divider {
    width: 1px;
    height: 78px;
    background: #294a7d;
    margin: 0;
}


/* SAĞ TARAF */

.main-weather-details {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px 12px;

    padding-left: 18px;
}


/* BİLGİ KARTLARI */

.weather-detail-item {
    background: rgba(255, 255, 255, 0.035);

    border: 1px solid rgba(
        96,
        165,
        250,
        0.15
    );

    border-radius: 11px;

    padding: 9px 10px;

    display: flex;
    align-items: center;

    gap: 9px;
}

.weather-detail-icon {
    font-size: 21px;
}

.weather-detail-title {
    color: #8fa4c7;
    font-size: 10px;
    margin-bottom: 2px;
}

.weather-detail-value {
    color: #f8fafc;
    font-size: 14px;
    font-weight: 700;
}
/* =================================================
   ŞEHİR ARAMA ALANI
   ================================================= */


[data-testid="stTextInput"] input:focus {
    border-color: #2f80ff !important;
    box-shadow: 0 0 0 1px #2f80ff !important;
}

/* Arama butonu */


button[kind="primary"] {
    background: linear-gradient(
        135deg,
        #ff2d68,
        #ff1760
    ) !important;

    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 700 !important;
    padding: 9px 18px !important;
    box-shadow: 0 5px 15px rgba(255, 45, 104, 0.25) !important;
}

button[kind="primary"]:hover {
    background: linear-gradient(
        135deg,
        #ff477a,
        #ff2d68
    ) !important;

    transform: translateY(-1px);
}
/* =================================================
   FAVORİ BUTONLARI
   ================================================= */

button:not([kind="primary"]) {
    border: 1px solid #1769d1 !important;
    background: #071a38 !important;
    color: #e8f1ff !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
}

button:not([kind="primary"]):hover {
    border-color: #2f80ff !important;
    background: #0d2850 !important;
    color: #ffffff !important;
}
/* =================================================
   PLANA GÖRE HAVA UYARILARI
   ================================================= */

.plan-alert-panel {
    background: linear-gradient(
        145deg,
        #071a3d,
        #0b2148
    );
    border: 1px solid #f0c929;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 18px;
    box-shadow: 0 0 18px rgba(240, 201, 41, 0.10);
}

.plan-alert-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 6px;
}

.plan-alert-icon {
    font-size: 27px;
}

.plan-alert-title {
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
}

.plan-alert-badge {
    background: #ff2d67;
    color: #ffffff;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 8px;
    border-radius: 12px;
}

.plan-alert-subtitle {
    color: #b9c9e8;
    font-size: 13px;
    margin-bottom: 14px;
}

.plan-warning {
    border: 1px solid #2169d1;
    background: rgba(13, 43, 88, 0.75);
    border-radius: 10px;
    padding: 13px;
    margin-top: 10px;
}

.plan-warning-sport {
    border-color: #d97919;
    background: rgba(55, 36, 20, 0.55);
    margin-top: 70px;
}
/* Gerçek hava uyarısı */
.plan-warning-danger {
    border-color: #ef4444;
    background: linear-gradient(
        145deg,
        rgba(127, 29, 29, 0.55),
        rgba(69, 10, 10, 0.45)
    );
    box-shadow: 0 0 12px rgba(239, 68, 68, 0.12);
}

/* Hava uygun kartı */
.plan-warning-safe {
    border-color: #22c55e;
    background: linear-gradient(
        145deg,
        rgba(20, 83, 45, 0.55),
        rgba(6, 45, 25, 0.45)
    );
    box-shadow: 0 0 12px rgba(34, 197, 94, 0.10);
}

.plan-warning-top {
    display: flex;
    align-items: center;
    gap: 12px;
}

.plan-warning-icon {
    font-size: 28px;
}

.plan-warning-title {
    color: #ffffff;
    font-size: 15px;
    font-weight: 700;
}

.plan-warning-time {
    color: #9fb9e8;
    font-size: 12px;
    margin-top: 2px;
}

.plan-warning-text {
    color: #dce7fa;
    font-size: 12px;
    line-height: 1.5;
    margin-top: 8px;
}

.plan-warning-arrow {
    margin-left: auto;
    color: #b77cff;
    font-size: 22px;
}
/* -------------------------------------------------
   ÜST BÖLÜMÜ SIKI VE DÜZENLİ HALE GETİR
------------------------------------------------- */

/* MeteoPlan başlığı */
h1 {
    margin-top: 0 !important;
    margin-bottom: 4px !important;
}

/* Konum satırı */
[data-testid="stAlert"] {
    margin-top: 8px !important;
    margin-bottom: 8px !important;
}
/* SAĞ PANEL BAŞLIKLARI */
.right-panel-title {
    font-size: 20px;
    font-weight: 700;
    color: #f5f7ff;
    margin-top: 8px;
    margin-bottom: 14px;
    padding: 12px 16px;
    border-radius: 14px;
    background: linear-gradient(
        135deg,
        rgba(30, 41, 82, 0.95),
        rgba(15, 23, 55, 0.95)
    );
    border: 1px solid rgba(90, 120, 255, 0.30);
    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.20),
        inset 0 0 20px rgba(70, 90, 180, 0.08);
}
/* GÜNLÜK NOT ALANI */
[data-testid="stTextArea"] textarea {
    background: rgba(12, 20, 45, 0.90) !important;
    color: #f5f7ff !important;
    border: 1px solid rgba(90, 120, 255, 0.35) !important;
    border-radius: 14px !important;
    min-height: 120px !important;
}

[data-testid="stTextArea"] textarea:focus {
    border-color: #6c7cff !important;
    box-shadow: 0 0 0 1px #6c7cff,
                0 0 18px rgba(108, 124, 255, 0.20) !important;
}

[data-testid="stSelectbox"] > div > div {
    background: rgba(12, 20, 45, 0.90) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(90, 120, 255, 0.30) !important;
}
/* AI PLAN KARTI */
.ai-plan-card {
    background: linear-gradient(
        135deg,
        rgba(20, 29, 65, 0.95),
        rgba(12, 19, 43, 0.95)
    );
    border: 1px solid rgba(108, 124, 255, 0.35);
    border-radius: 16px;
    padding: 18px;
    margin-top: 10px;
    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.20),
        inset 0 0 25px rgba(90, 110, 220, 0.06);
}

.ai-plan-title {
    font-size: 16px;
    font-weight: 700;
    color: #8ea2ff;
    margin-bottom: 12px;
}

.ai-plan-content {
    color: #e8ecff;
    font-size: 14px;
    line-height: 1.7;
}
/* KAYITLI NOTLAR */
.saved-note-item {
    background: linear-gradient(
        135deg,
        rgba(20, 29, 65, 0.95),
        rgba(12, 19, 43, 0.95)
    );
    border: 1px solid rgba(90, 120, 255, 0.25);
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 10px;
    box-shadow:
        0 8px 22px rgba(0, 0, 0, 0.16);
}

.saved-note-hour {
    color: #8ea2ff;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 7px;
}

.saved-note-text {
    color: #f2f4ff;
    font-size: 14px;
    line-height: 1.5;
}

.saved-note-meta {
    color: #8993b5;
    font-size: 12px;
    margin-top: 9px;
}
/* HAVA UYARI KARTLARI */
.warning-card {
    background: linear-gradient(
        135deg,
        rgba(35, 28, 60, 0.95),
        rgba(18, 20, 48, 0.95)
    );
    border: 1px solid rgba(255, 105, 180, 0.30);
    border-radius: 15px;
    padding: 15px 16px;
    margin-bottom: 10px;
    box-shadow:
        0 8px 24px rgba(0, 0, 0, 0.18);
}

.warning-card-title {
    color: #ff8fc7;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 6px;
}

.warning-card-text {
    color: #e8eaff;
    font-size: 13px;
    line-height: 1.6;
}
/* SAĞ PANEL GENEL DÜZEN */
[data-testid="column"] {
    gap: 0.8rem;
}

.right-panel-title {
    margin-top: 4px;
    margin-bottom: 10px;
}


/* ŞEHİR ARAMA - STREAMLIT KAPSAYICI */
[data-testid="stTextInput"] [data-baseweb="input"] {
    background-color: #0d1935 !important;
    border: 1px solid #2859a8 !important;
    border-radius: 10px !important;
}

[data-testid="stTextInput"] [data-baseweb="base-input"] {
    background-color: #0d1935 !important;
}


/* ŞEHİR ARAMA ALANI */
[data-testid="stTextInput"] {
    margin-top: 2px !important;
    margin-bottom: 8px !important;
}

[data-testid="stTextInput"] label {
    color: #c7d5ed !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    margin-bottom: 5px !important;
}

[data-testid="stTextInput"] input {
    height: 42px !important;
    padding: 0 14px !important;
    border-radius: 9px !important;
    font-size: 14px !important;
}
.location-card {
    background: linear-gradient(
        145deg,
        #0d2d68,
        #0b2452
    );

    border: 1px solid #1769d1;
    border-radius: 10px;

    color: #f8fafc;
    font-size: 14px;
    font-weight: 600;

    padding: 10px 14px;
    margin-top: 8px;
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

import pandas as pd
import altair as alt
from weather import get_weather, weather_code_to_text
from ai import generate_daily_plan
from database import (
    save_weather_history,
    get_weather_history,
    save_note,
    get_notes,
    delete_note,
    add_favorite,
    get_favorites,
    delete_favorite
)

if "weather_data" not in st.session_state:
    st.session_state.weather_data = None

if "daily_plan" not in st.session_state:
    st.session_state.daily_plan = None

if "city_name" not in st.session_state:
    st.session_state.city_name = ""

# ANA SAYFA SÜTUNLARI
sol, sag = st.columns([1.25, 1])
with sol:
    # -------------------------------------------------
    # BAŞLIK
    # -------------------------------------------------

    st.html(
        """
        <div class="meteo-header">
    
            <div class="meteo-logo">
                🌤️
            </div>
    
            <div>
                <div class="meteo-brand">
                    MeteoPlan
                </div>
    
                <div class="meteo-subtitle">
                    Hava durumuna göre gününü planla.
                </div>
            </div>
    
        </div>
        """
    )


    # -------------------------------------------------
    # ŞEHİR ARAMA
    # -------------------------------------------------


    city = st.text_input(
        "Şehir adı",
        placeholder="Örneğin: Yalova, İstanbul, Ankara..."
    )

    search_button = st.button(
        "🔍 Hava Durumunu Getir",
        type="primary"
    )
    if search_button:
        st.session_state.favorite_search = False

    if st.session_state.get("favorite_search", False):
        city = st.session_state.favorite_city
        search_button = True
    # -------------------------------------------------
    # FAVORİ ŞEHİRLER
    # -------------------------------------------------

    favorites = get_favorites()

    if favorites:

        if st.button(
                "❤️ Favori Şehirler",
                key="favorite_cities_button"
        ):

            st.session_state.show_favorites = not st.session_state.get(
                "show_favorites",
                False
            )

        if st.session_state.get("show_favorites", False):

            favorite_columns = st.columns(
                min(len(favorites), 4)
            )

            for index, favorite in enumerate(favorites):

                favorite_id = favorite[0]
                favorite_city = favorite[1]

                with favorite_columns[index % 4]:

                    st.markdown(
                        f"""
                        <div class="favorite-city-card">
                            <div class="favorite-city-icon">❤️</div>
                            <div class="favorite-city-name">
                                {favorite_city}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button(
                            "🌤️ Hava Durumunu Getir",
                            key=f"favorite_weather_{index}"
                    ):
                        st.session_state.city_name = favorite_city
                        st.session_state.favorite_city = favorite_city
                        st.session_state.favorite_search = True
                        st.rerun()

                    if st.button(
                            "💔 Favorilerden Çıkar",
                            key=f"delete_favorite_{index}"
                    ):
                        delete_favorite(favorite_id)
                        st.rerun()


    # -------------------------------------------------
    # HAVA DURUMU
    # -------------------------------------------------


        if search_button or st.session_state.weather_data is not None:

            if not city.strip():
                st.warning("Lütfen bir şehir adı girin.")

            else:

                try:

                    with st.spinner("Hava durumu getiriliyor..."):

                        weather = get_weather(city.strip())
                    if weather:
                        st.session_state.weather_data = weather

                    if weather is None:

                        st.error(
                        "Bu şehir bulunamadı. "
                        "Lütfen şehir adını kontrol edin."
                        )

                    else:

                        location = weather["location"]
                        current = weather["current"]

                        city_name = location["name"]
                        st.session_state.city_name = city_name

                        # -------------------------------------------------
                        # FAVORİYE EKLE
                        # -------------------------------------------------

                        if st.button(
                                "❤️ Favorilere Ekle",
                                key="add_favorite_button"
                        ):
                            add_favorite(city_name)
                            st.success(
                                f"❤️ {city_name} favorilere eklendi."
                            )

                            st.markdown(
                                "<div style='height: 2px;'></div>",
                                unsafe_allow_html=True
                            )

                        country = location["country"]

                        temperature = current.get(
                            "temperature_2m"
                        )

                        apparent_temperature = current.get(
                            "apparent_temperature"
                        )

                        humidity = current.get(
                            "relative_humidity_2m"
                        )

                        wind_speed = current.get(
                            "wind_speed_10m"
                        )

                        visibility = current.get(
                            "visibility"
                        )

                        weather_code = current.get(
                            "weather_code"
                        )

                        description = weather_code_to_text(
                            weather_code
                        )

                        # -----------------------------
                        # KONUM
                        # -----------------------------

                        st.markdown(
                            f"""
                            <div class="location-card">
                                📍 {city_name}, {country}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        # -----------------------------
                        # MODERN HAVA BİLGİ KARTLARI
                        # -----------------------------
                        st.html(
                            f"""
                            <div class="main-weather-card">
    
                                <div class="main-weather-left">
    
                                    <div class="main-weather-icon">
                                        🌤️
                                    </div>
    
                                    <div>
                                        <div class="main-temperature">
                                            {temperature}°C
                                        </div>
    
                                        <div class="main-weather-description">
                                            {description}
                                        </div>
                                    </div>
    
                                </div>
    
                                <div class="main-weather-divider"></div>
    
                                <div class="main-weather-details">
    
                                    <div class="weather-detail-item">
                                        <div class="weather-detail-icon">🌡️</div>
                                        <div>
                                            <div class="weather-detail-title">
                                                Hissedilen
                                            </div>
                                            <div class="weather-detail-value">
                                                {apparent_temperature}°C
                                            </div>
                                        </div>
                                    </div>
    
                                    <div class="weather-detail-item">
                                        <div class="weather-detail-icon">💧</div>
                                        <div>
                                            <div class="weather-detail-title">
                                                Nem
                                            </div>
                                            <div class="weather-detail-value">
                                                %{humidity}
                                            </div>
                                        </div>
                                    </div>
    
                                    <div class="weather-detail-item">
                                        <div class="weather-detail-icon">💨</div>
                                        <div>
                                            <div class="weather-detail-title">
                                                Rüzgâr
                                            </div>
                                            <div class="weather-detail-value">
                                                {wind_speed} km/sa
                                            </div>
                                        </div>
                                    </div>

                                    <div class="weather-detail-item">
                                        <div class="weather-detail-icon">👁️</div>
                                        <div>
                                            <div class="weather-detail-title">
                                            Görüş
                                        </div>
                                        <div class="weather-detail-value">
                                            {f"{visibility / 1000:.1f} km" if visibility is not None else "—"}
                                            </div>
                                        </div>
                                    </div>

                                </div>

                            </div>
                             """
                        )

                    # -----------------------------
                    # SAATLİK TAHMİN
                    # -----------------------------

                        st.subheader("🕐 Saatlik Hava Durumu")

                        weather = st.session_state.get("weather_data") or {}
                        hourly = weather.get("hourly", {})

                        hourly_times = hourly.get("time", [])
                        hourly_temperatures = hourly.get(
                            "temperature_2m", []
                        )
                        hourly_precipitation = hourly.get(
                            "precipitation_probability", []
                        )
                        hourly_weather_codes = hourly.get(
                            "weather_code", []
                        )

                        if hourly_times:

                            # Mevcut saatten sonraki 12 saati göster
                            current_time = current.get("time", "")

                            start_index = 0

                            for i, time_value in enumerate(hourly_times):
                                if time_value[:13] >= current_time[:13]:
                                    start_index = i
                                    break

                            hourly_data = []

                            for i in range(
                                    start_index,
                                    min(start_index + 12, len(hourly_times))
                            ):
                                time_value = hourly_times[i]

                                # 2026-09-30T14:00
                                # → 14:00
                                time_text = time_value[-5:]

                                temperature_value = (
                                    hourly_temperatures[i]
                                    if i < len(hourly_temperatures)
                                    else None
                                )

                                precipitation_value = (
                                    hourly_precipitation[i]
                                    if i < len(hourly_precipitation)
                                    else None
                                )

                                weather_code_value = (
                                    hourly_weather_codes[i]
                                    if i < len(hourly_weather_codes)
                                    else None
                                )

                                weather_text = (
                                    weather_code_to_text(
                                        weather_code_value
                                    )
                                )

                                hourly_data.append({
                                    "Saat": time_text,
                                    "Hava": weather_text,
                                    "Sıcaklık": (
                                        f"{temperature_value} °C"
                                    ),
                                    "Yağış İhtimali": (
                                        f"%{precipitation_value}"
                                        if precipitation_value is not None
                                        else "-"
                                    )
                                })

                            hourly_cards_html = ""

                            for item in hourly_data:

                                weather_text = item["Hava"]

                                if "Yağmur" in weather_text:
                                    weather_icon = "🌧️"
                                elif "Kar" in weather_text:
                                    weather_icon = "❄️"
                                elif "Fırtına" in weather_text:
                                    weather_icon = "⛈️"
                                elif "Bulutlu" in weather_text:
                                    weather_icon = "☁️"
                                elif "Açık" in weather_text:
                                    weather_icon = "☀️"
                                else:
                                    weather_icon = "🌤️"

                                hourly_cards_html += f"""
                            <div class="hourly-card">
                                <div class="hourly-time">{item["Saat"]}</div>
                                <div class="hourly-icon">{weather_icon}</div>
                                <div class="hourly-temperature">{item["Sıcaklık"]}</div>
                                <div class="hourly-weather">{weather_text}</div>
                                <div class="hourly-rain">💧 {item["Yağış İhtimali"]}</div>
                            </div>
                            """

                            st.markdown(
                                f"""
                            <div class="hourly-scroll">
                                {hourly_cards_html}
                            </div>
                            """,
                                unsafe_allow_html=True
                            )
                            # -----------------------------
                            # SICAKLIK GRAFİĞİ
                            # -----------------------------

                            st.subheader(
                                "📈 Saatlik Sıcaklık Grafiği"
                            )

                            chart_end = min(
                                start_index + 12,
                                len(hourly_times),
                                len(hourly_temperatures)
                            )

                            chart_times = [
                                pd.to_datetime(hourly_times[i])
                                for i in range(start_index, chart_end)
                            ]

                            chart_temperatures = [
                                hourly_temperatures[i]
                                for i in range(start_index, chart_end)
                            ]

                            chart_data = pd.DataFrame({
                                "Saat": chart_times,
                                "Sıcaklık (°C)": chart_temperatures
                            })

                            chart = (
                                alt.Chart(chart_data)
                                .mark_line(point=True)
                                .encode(
                                    x=alt.X(
                                        "Saat:T",
                                        title="Saat",
                                        axis=alt.Axis(format="%H:%M")
                                    ),
                                    y=alt.Y(
                                        "Sıcaklık (°C):Q",
                                        title="Sıcaklık (°C)"
                                    ),
                                    tooltip=[
                                        alt.Tooltip(
                                            "Saat:T",
                                            title="Saat",
                                            format="%H:%M"
                                        ),
                                        alt.Tooltip(
                                            "Sıcaklık (°C):Q",
                                            title="Sıcaklık (°C)"
                                        )
                                    ]
                                )
                                .properties(
                                    height=300
                                )
                            )

                            st.altair_chart(
                                chart,
                                use_container_width=True
                            )


                        else:

                            st.info(

                                "Saatlik tahmin verisi bulunamadı."

                            )




                except Exception as error:

                    st.error(
                    f"Hava durumu alınırken bir hata oluştu: {error}"
                )



with sag:
    # -------------------------------------------------
    # PLANA GÖRE HAVA UYARILARI
    # -------------------------------------------------

    weather = st.session_state.get("weather_data") or {}

    hourly = weather.get("hourly", {})

    hourly_times = hourly.get("time", [])
    hourly_precipitation = hourly.get(
        "precipitation_probability",
        []
    )
    hourly_wind = hourly.get(
        "wind_speed_10m",
        []
    )
    hourly_weather_codes = hourly.get(
        "weather_code",
        []
    )

    city_name = st.session_state.get(
        "city_name",
        city
    )

    # -------------------------------------------------
    # KAYITLI NOTLARI AL
    # -------------------------------------------------

    saved_notes = get_notes(city_name)

    warnings = []

    if saved_notes and hourly_times:

        for note in saved_notes:

            note_id, note_city, note_hour, note_text, created_at = note

            note_text_lower = note_text.lower()

            # -------------------------------------------------
            # AKTİVİTE TÜRÜNÜ BELİRLE
            # -------------------------------------------------

            if any(
                    word in note_text_lower
                    for word in [
                        "yürüyüş",
                        "yurumek",
                        "yürüyeceğim",
                        "yürüyüşe"
                    ]
            ):

                activity_title = "Yürüyüş Planı"
                activity_icon = "🚶"

            elif any(
                    word in note_text_lower
                    for word in [
                        "spor",
                        "koşu",
                        "koşacağım",
                        "bisiklet",
                        "fitness",
                        "egzersiz",
                        "gym"
                    ]
            ):

                activity_title = "Spor Planı"
                activity_icon = "🏃"

            else:

                activity_title = "Günlük Plan"
                activity_icon = "📝"

            # -------------------------------------------------
            # NOT SAATİNİ BUL
            # -------------------------------------------------

            note_index = None

            for i, time_value in enumerate(hourly_times):

                if time_value[-5:] == note_hour:
                    note_index = i
                    break

            if note_index is None:
                continue

            # -------------------------------------------------
            # HAVA VERİLERİNİ AL
            # -------------------------------------------------

            precipitation = (
                hourly_precipitation[note_index]
                if note_index < len(hourly_precipitation)
                else 0
            )

            wind_value = (
                hourly_wind[note_index]
                if note_index < len(hourly_wind)
                else 0
            )

            weather_code = (
                hourly_weather_codes[note_index]
                if note_index < len(hourly_weather_codes)
                else None
            )

            # -------------------------------------------------
            # YAĞIŞ KONTROLÜ
            # -------------------------------------------------

            rainy_weather = (
                    weather_code is not None
                    and (
                            51 <= weather_code <= 67
                            or 80 <= weather_code <= 82
                            or 95 <= weather_code <= 99
                    )
            )

            rain_warning = (
                                   precipitation is not None
                                   and precipitation >= 50
                           ) or rainy_weather

            # -------------------------------------------------
            # RÜZGAR KONTROLÜ
            # -------------------------------------------------

            wind_warning = (
                    wind_value is not None
                    and wind_value >= 25
            )

            # -------------------------------------------------
            # UYARI OLUŞTUR
            # -------------------------------------------------

            if rain_warning or wind_warning:

                warning_messages = []

                if rain_warning:
                    probability_text = (
                        f"%{precipitation}"
                        if precipitation is not None
                        else "yüksek"
                    )

                    warning_messages.append(
                        f"Bu saatte yağış ihtimali "
                        f"{probability_text}."
                    )

                if wind_warning:
                    warning_messages.append(
                        f"Rüzgar hızı "
                        f"{wind_value:.1f} km/sa olacak."
                    )

                warning_messages.append(
                    "Planını hava durumuna göre gözden geçirmen iyi olur."
                )

                warnings.append(
                    {
                        "title": activity_title,
                        "icon": activity_icon,
                        "time": note_hour,
                        "text": "<br>".join(warning_messages)
                    }
                )

    # -------------------------------------------------
    # UYARI PANELİ
    # -------------------------------------------------

    warning_count = len(warnings)

    if warning_count > 0:

        alert_html = f"""
        <div class="plan-alert-panel">

            <div class="plan-alert-header">

                <div class="plan-alert-icon">
                    🔔
                </div>

                <div class="plan-alert-title">
                    Plana Göre Hava Uyarıları
                </div>

                <div class="plan-alert-badge">
                    {warning_count} Uyarı
                </div>

            </div>

            <div class="plan-alert-subtitle">
                Kayıtlı planlarına göre hava durumu seni uyarıyor.
            </div>
        """

        for warning in warnings:
            alert_html += f"""
                <div class="plan-warning plan-warning-danger">

                    <div class="plan-warning-top">

                    <div class="plan-warning-icon">
                        {warning["icon"]}
                    </div>

                    <div>

                        <div class="plan-warning-title">
                            {warning["title"]}
                        </div>

                        <div class="plan-warning-time">
                            {warning["time"]}
                        </div>

                    </div>

                    <div class="plan-warning-arrow">
                        ›
                    </div>

                </div>

                <div class="plan-warning-text">
                    {warning["text"]}
                </div>

            </div>
            """

        alert_html += """
        </div>
        """

        st.html(alert_html)


    else:

        # Kayıtlı planları göster

        plan_count = len(saved_notes) if saved_notes else 0

        alert_html = f"""

        <div class="plan-alert-panel">


            <div class="plan-alert-header">


                <div class="plan-alert-icon">

                    🔔

                </div>


                <div class="plan-alert-title">

                    Plana Göre Hava Uyarıları

                </div>


                <div class="plan-alert-badge">

                    {plan_count} Plan

                </div>


            </div>


            <div class="plan-alert-subtitle">

                Kayıtlı planlarına göre hava durumu kontrol edildi.

            </div>

        """

        if saved_notes:

            for note in saved_notes:

                note_id, note_city, note_hour, note_text, created_at = note

                note_text_lower = note_text.lower()

                # Aktivite türünü belirle

                if any(

                        word in note_text_lower

                        for word in [

                            "yürüyüş",

                            "yurumek",

                            "yürüyeceğim",

                            "yürüyüşe"

                        ]

                ):

                    activity_title = "Yürüyüş Planı"

                    activity_icon = "🚶"


                elif any(

                        word in note_text_lower

                        for word in [

                            "spor",

                            "koşu",

                            "koşacağım",

                            "bisiklet",

                            "fitness",

                            "egzersiz",

                            "gym"

                        ]

                ):

                    activity_title = "Spor Planı"

                    activity_icon = "🏃"


                else:

                    activity_title = "Günlük Plan"

                    activity_icon = "📝"

                alert_html += f"""

                <div class="plan-warning">


                    <div class="plan-warning-top">


                        <div class="plan-warning-icon">

                            {activity_icon}

                        </div>


                        <div>


                            <div class="plan-warning-title">

                                {activity_title}

                            </div>


                            <div class="plan-warning-time">

                                {note_hour}

                            </div>


                        </div>


                        <div class="plan-warning-arrow">

                            ✓

                        </div>


                    </div>


                    <div class="plan-warning-text">

                        Hava uygun görünüyor.<br>

                        Planına devam edebilirsin.

                    </div>


                </div>

                """


        else:

            alert_html += """

            <div class="plan-warning plan-warning-safe">


                <div class="plan-warning-top">


                    <div class="plan-warning-icon">

                        📝

                    </div>


                    <div>


                        <div class="plan-warning-title">

                            Henüz Plan Yok

                        </div>


                        <div class="plan-warning-time">

                            Günlük Not

                        </div>


                    </div>


                </div>


                <div class="plan-warning-text">

                    Günlük Not kısmından bir plan eklediğinde

                    burada otomatik olarak gösterilecek.

                </div>


            </div>

            """

        alert_html += """

        </div>

        """

        st.html(alert_html)

    # -------------------------------------------------

    # NOT EKLEME

    # -------------------------------------------------

    st.markdown(
        """
        <div class="right-panel-title">
            📝 Günlük Not
        </div>
        """,
        unsafe_allow_html=True
    )


    weather = st.session_state.get("weather_data") or {}
    hourly = weather.get("hourly", {})

    hourly_times = hourly.get("time", [])

    current = weather.get("current", {})
    current_time = current.get("time", "")

    start_index = 0

    for i, time_value in enumerate(hourly_times):
        if time_value[:13] >= current_time[:13]:
            start_index = i
            break

    city_name = st.session_state.get(
        "city_name",
        city
    )

    if hourly_times:
        with st.form("note_form"):

            note_hour = st.selectbox(
                "Not için saat seç",
                [
                    hourly_times[i][-5:]
                    for i in range(
                    start_index,
                    min(
                        start_index + 12,
                        len(hourly_times)
                    )
                )
                ]
            )

            note_text = st.text_area(
                "Notunuzu yazın",
                placeholder=(
                    "Örneğin: Bu saatte yürüyüş yapacağım..."
                )
            )

            save_note_button = st.form_submit_button(
                "💾 Notu Kaydet"
            )

            if save_note_button:

                if not note_text.strip():

                    st.warning(
                        "Lütfen bir not yazın."
                    )

                else:

                    save_note(
                        city_name,
                        note_hour,
                        note_text.strip()
                    )

                    st.success(
                        "✅ Notunuz SQLite "
                        "veritabanına kaydedildi."
                    )

                    st.rerun()

    # -----------------------------

    # AI GÜNLÜK PLAN

    # -----------------------------

    st.markdown(
        """
        <div class="right-panel-title">
            ✨ MeteoPlan AI
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("✨ AI ile Günlük Plan Oluştur"):

        weather = st.session_state.get("weather_data")

        if not weather:
            st.warning(
                "Önce bir şehir aratıp hava durumunu getirmeniz gerekiyor."
            )

        else:
            current = weather.get("current", {})

            temperature = current.get("temperature_2m")
            humidity = current.get("relative_humidity_2m")
            wind_speed = current.get("wind_speed_10m")

            weather_code = current.get("weather_code")
            description = weather_code_to_text(weather_code)

            city_name = st.session_state.get(
                "city_name",
                city
            )

            try:
                with st.spinner("AI günlük planını hazırlıyor..."):

                    st.session_state.daily_plan = generate_daily_plan(
                        city_name,
                        temperature,
                        description,
                        humidity,
                        wind_speed
                    )

            except Exception as error:

                st.error(
                    f"AI planı oluşturulurken bir hata oluştu: {error}"
                )

    if st.session_state.daily_plan:
        plan_text = (
            st.session_state.daily_plan
            .replace("### ", "")
            .replace("**", "")
            .replace("* ", "")
            .replace("\n", "<br>")
        )

        st.markdown(
            f"""<div class="ai-plan-card">
                        <div class="ai-plan-title">✨ MeteoPlan Günlük Önerisi</div>
                        <div class="ai-plan-content">{plan_text}</div>
                        </div>""",
            unsafe_allow_html=True
        )
    # -------------------------------------------------
    # KAYITLI NOTLAR
    # -------------------------------------------------

    st.markdown(
        """
        <div class="right-panel-title">
            📚 Kayıtlı Notlar
        </div>
        """,
        unsafe_allow_html=True
    )
    city_name = st.session_state.get("city_name", city)

    saved_notes = get_notes(city_name)

    if saved_notes:

        for note in saved_notes:

            note_id, note_city, note_hour, note_text, created_at = note

            col1, col2 = st.columns([6, 2])

            with col1:

                st.markdown(
                    f"""<div class="saved-note-item">
                    <div class="saved-note-hour">
                    🕐 {note_hour}
                    </div>
                    <div class="saved-note-text">
                    {note_text}
                    </div>
                    <div class="saved-note-meta">
                    📍 {note_city} &nbsp;|&nbsp; 🗓️ {created_at}
                    </div>
                    </div>""",
                    unsafe_allow_html=True
                )

            with col2:

                if st.button(
                        "🗑️ Sil",
                        key=f"delete_note_{note_id}"
                ):
                    delete_note(note_id)

                    st.success("✅ Not silindi.")

                    st.rerun()

    else:

        st.write(
            "Henüz kayıtlı bir not bulunmuyor."
        )

    # -----------------------------
    # VERİTABANINA KAYDET
    # -----------------------------
    if search_button and st.session_state.get("weather_data"):
        save_weather_history(
            city_name,
            country,
            temperature,
            description
        )

        st.info(
            "🔒 Bu hava durumu araması "
            "SQLite geçmişine kaydedildi."
        )




# -----------------------------
# HAVA DURUMU GEÇMİŞİ
# -----------------------------

st.divider()

st.subheader("📚 Hava Durumu Geçmişi")

history = get_weather_history()

if history:

    history_html = ""

    for row in history:

        history_html += f"""
<tr>
    <td>{row[0]}</td>
    <td>{row[1]}</td>
    <td>{row[2]} °C</td>
    <td>{row[3]}</td>
    <td>{row[4]}</td>
</tr>
"""

    st.markdown(
        f"""<div class="history-card">
<table class="history-table">
<thead>
<tr>
    <th>Şehir</th>
    <th>Ülke</th>
    <th>Sıcaklık</th>
    <th>Hava Durumu</th>
    <th>Arama Tarihi</th>
</tr>
</thead>
<tbody>
{history_html}
</tbody>
</table>
</div>""",
        unsafe_allow_html=True
    )

else:

    st.info(
        "Henüz kayıtlı hava durumu geçmişi bulunmuyor."
    )


# -------------------------------------------------
# ALT BİLGİ
# -------------------------------------------------

st.divider()

st.caption(
    "MeteoPlan • Hava durumuna göre gününü planla."
)