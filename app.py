"""
Copilot, aşağıdaki talimatlara göre bir Streamlit uygulaması oluştur:
- Hafıza yönetimi (memory.json)
- Günün cümlesi (her gün değişen motivasyon mesajı)
- Gemini AI sohbet entegrasyonu (gemini-pro modeli)
- Kullanıcı arayüzü Streamlit ile oluşturulacak
- Kullanıcıya hafıza geçmişini gösterme seçeneği eklenecek
- Kod fonksiyonel olacak ve şu ana fonksiyonlara ayrılacak:
  - load_memory: Hafıza dosyasını yükler
  - save_memory: Hafızayı dosyaya kaydeder
  - ask_gemini: Gemini modeline istek gönderir
  - get_daily_quote: Günün cümlesini döndürür
  - main: Streamlit arayüzünü yönetir
"""

import streamlit as st
from datetime import datetime
import os
import google.generativeai as genai
import json
from typing import List, Dict, Any
from PIL import Image
import base64

def get_base64_from_file(file_path):
    """Dosyayı base64 formatına çevirir"""
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception as e:
        print(f"Logo okuma hatası: {e}")
        return ""

# --------------------
# Gemini API Ayarı
# --------------------
GEMINI_API_KEY = "AIzaSyCSmY3zGNJ8iaB4IRxlz-rLgg-F-m-cuzU"  # Sabit API anahtarı

# API yapılandırması
try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    print(f"API yapılandırma hatası: {e}")

def configure_api(api_key: str) -> bool:
    """API anahtarını yapılandırır ve test eder"""
    global GEMINI_API_KEY
    try:
        # API anahtarını güncelle ve yapılandır
        GEMINI_API_KEY = api_key


        genai.configure(api_key=api_key)
        
        # Safety settings ile test yap
        model = genai.GenerativeModel('gemini-pro',
            safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            ]
        )
        
        response = model.generate_content("Merhaba")
        
        if response and response.text:
            return True
        else:
            print("Hata: API yanıt vermedi")
            return False
    except Exception as e:
        error_msg = str(e)
        if "invalid api key" in error_msg.lower():
            print("Hata: Geçersiz API anahtarı")
        elif "permission denied" in error_msg.lower():
            print("Hata: API erişim izni reddedildi")
        elif "quota" in error_msg.lower():
            print("Hata: API kota sınırı aşıldı")
        else:
            print(f"API yapılandırma hatası: {error_msg}")
        return False

# --------------------
# Hafıza Dosyası
# --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "memory.json")

# Dizin oluştur
os.makedirs(BASE_DIR, exist_ok=True)

def load_memory() -> List[Dict[str, Any]]:
    """Memory.json dosyasını yükler, yoksa boş liste döner.

    Hafıza formatı: liste içinde sözlükler: {"role": "user"|"assistant", "content": str, "ts": isoformat}
    Eğer eski format (sadece stringler) bulunursa, alternatif sıraya göre dönüştürülür.
    """
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []

    # Eğer zaten yeni formatta ise doğrudan döndür
    if isinstance(data, list) and all(isinstance(i, dict) and "role" in i and "content" in i for i in data):
        return data

    # Eğer eski format: sadece stringler (alternating user/assistant), dönüştür
    if isinstance(data, list) and all(isinstance(i, str) for i in data):
        converted: List[Dict[str, Any]] = []
        for idx, text in enumerate(data):
            role = "user" if idx % 2 == 0 else "assistant"
            converted.append({"role": role, "content": text, "ts": None})
        return converted

    return []

def save_memory(memory: List[Dict[str, Any]]) -> None:
    """Hafızayı memory.json dosyasına kaydeder (UTF-8)."""
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(memory, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Hafıza kaydedilirken hata oluştu: {e}")

# --------------------
# Günün Cümlesi
# --------------------
def get_daily_quote():
    """Her gün farklı bir motivasyon cümlesi döner"""
    quotes = [
        "Bugün harika bir gün olabilir, sen izin ver!",
        "Her küçük adım büyük bir yolculuğun başlangıcıdır.",
        "Olumsuzlukları bırak, pozitif enerjiyi kucakla.",
        "Hayat bir macera, cesur ol ve tadını çıkar.",
        "Küçük başarıları kutlamak büyük motivasyondur.",
        "Hayatındaki en iyi versiyonunu oluşturmaya bugün başla.",
        "Odaklan, planla ve istikrarlı ol; sonuçlar gelir.",
        "Kendine karşı nazik ol; ilerleme bazen küçük adımlarla gelir.",
        "Her yeni gün, yeni bir başlangıç şansıdır.",
        "Zorluklar seni güçlendirir, vazgeçme!",
        "İnanmak başarmanın yarısıdır.",
        "En karanlık gece bile güneşin doğuşuyla sona erer.",
        "Bugün dünden daha güçlüsün.",
        "Başarı yolculuktur, varış noktası değil.",
        "Her şey zihninde başlar, olumlu düşün.",
        "Sınırlarını zorla, konfor alanından çık.",
        "Düşlerine inan, onları gerçekleştirmek için çabala.",
        "Değişim senin elinde, harekete geç.",
        "En büyük zafer kendini aşmaktır.",
        "Her başarısızlık yeni bir öğrenme fırsatıdır."
    ]
    # Günün numarasına göre deterministik seçim
    day_index = datetime.now().date().toordinal() % len(quotes)
    return quotes[day_index]

# --------------------
# Gemini Chat Fonksiyonu
# --------------------
def ask_gemini(prompt: str, memory: List[Dict[str, Any]]) -> str:
    """Kullanıcı mesajını alır, son 10 hafıza kaydını ekler ve Gemini'den cevap alır."""
    if not GEMINI_API_KEY:
        raise RuntimeError("Gemini API anahtarı ayarlı değil. Lütfen API anahtarını girin.")

    try:
        # Model oluştur
        model = genai.GenerativeModel('gemini-2.0-flash')

        # Mesajı hazırla
        message = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }
        
        # Sistem talimatı ve bağlamı ekle
        system_prompt = "Sen Civbot adında yardımcı ve nazik bir asistanısın. Kısa, net ve yardımcı cevaplar ver."
        full_prompt = f"{system_prompt}\n\nSoru: {prompt}"
        
        # Mesajı hazırla
        message = {
            "contents": [{
                "parts": [{
                    "text": full_prompt
                }]
            }]
        }
        
        # Yanıt al
        response = model.generate_content(full_prompt)
        
        if not response.text:
            raise RuntimeError("API yanıt vermedi")
            
        return response.text.strip()
    except Exception as e:
        # Daha detaylı hata mesajı
        error_msg = str(e)
        if "not found for API version" in error_msg:
            raise RuntimeError("API erişim hatası: Lütfen API anahtarınızın doğru olduğunu ve hesabınızın Gemini API'ye erişim iznine sahip olduğunu kontrol edin.")
        elif "quota" in error_msg.lower():
            raise RuntimeError("API kota hatası: Günlük kullanım limitinize ulaştınız veya hesabınız henüz aktif değil.")
        else:
            raise RuntimeError(f"Gemini API hatası: {error_msg}")

# --------------------
# Streamlit Arayüzü
# --------------------
def main():
    global GEMINI_API_KEY
    
    logo_path = os.path.join(os.getcwd(), "logo.png")
    page_icon = Image.open(logo_path) if os.path.exists(logo_path) else "🤖"
    st.set_page_config(
        page_title="Civbot - Hafıza ve Günün Cümlesi Asistanı", 
        page_icon=page_icon, 
        layout="centered"
    )
    
    # Tema durumunu session state'de tut
    if 'theme' not in st.session_state:
        st.session_state.theme = 'dark'  # Varsayılan tema

    # Tema değiştirme butonu - Sağ üst köşede
    col1, col2 = st.columns([6, 1])
    with col2:
        theme_button = '🌙' if st.session_state.theme == 'light' else '☀️'
        if st.button(theme_button, key='theme_toggle'):
            st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'
            st.rerun()

    # Modern UI stil tanımlamaları
    dark_mode = st.session_state.theme == 'dark'
    st.markdown(f"""
        <style>
        /* Tema değişkenleri */
        :root {{
            --bg-primary: {('#0A0F1E' if dark_mode else '#F8FAFC')};
            --bg-secondary: {('#111827' if dark_mode else '#FFFFFF')};
            --text-primary: {('#F5F7FA' if dark_mode else '#1E293B')};
            --text-secondary: {('#94A3B8' if dark_mode else '#475569')};
            --label-color: {('#F5F7FA' if dark_mode else '#1E293B')};
            --accent-color: #00AEEF;
            --accent-hover: #0EA5E9;
            --border-color: {('#1E293B' if dark_mode else '#CBD5E1')};
            --input-text: {('#F5F7FA' if dark_mode else '#1E293B')};
            --shadow-color: {'rgba(0,174,239,0.1)' if dark_mode else 'rgba(14,165,233,0.1)'};
            --text-label: {('#E2E8F0' if dark_mode else '#1E293B')};
            --text-muted: {('#94A3B8' if dark_mode else '#64748B')};
        }}

        /* Geçiş Efektleri */
        * {{
            transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease !important;
        }}

        /* Ana Stiller */
        .stApp {{
            background-color: var(--bg-primary) !important;
        }}
        
        /* Başlık Container */
        .header-container {{
            display: flex;
            align-items: center;
            background-color: var(--bg-secondary);
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 12px var(--shadow-color);
        }}
        
        /* Logo */
        .header-logo {{
            width: 80px;
            margin-right: 24px;
            filter: drop-shadow(0 0 8px var(--shadow-color));
        }}
        
        /* Başlık */
        .header-title {{
            background: linear-gradient(90deg, var(--accent-color), var(--accent-hover));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 34px;
            font-weight: 700;
            margin: 0;
            padding: 0;
            font-family: 'Inter', sans-serif;
        }}
        
        /* Günün Sözü */
        .daily-quote {{
            color: #00AEEF;
            font-style: italic;
            font-weight: 500;
            text-align: center;
            padding: 1rem;
            background: {('rgba(17,24,39,0.6)' if dark_mode else '#E0F2FE')};
            border-radius: 12px;
            margin: 1rem 0;
            border: 1px solid {('#1E293B' if dark_mode else '#BAE6FD')};
        }}
        
        /* Mesaj Alanı */
        .stTextArea > div > div,
        .st-ae.st-bd.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm {{
            background-color: var(--bg-secondary) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 12px !important;
            color: {('#FFFFFF' if dark_mode else '#000000')} !important;
            font-family: "Source Sans", sans-serif !important;
            font-size: 16px !important;
            line-height: 1.5 !important;
        }}
        
        /* Label Renkleri */
        .stTextArea label {{
            color: var(--text-label) !important;
            font-family: "Source Sans", sans-serif !important;
            font-size: 16px !important;
            font-weight: 500 !important;
        }}
        
        div[data-baseweb="textarea"],
        textarea#text_area,
        .st-ae.st-bd.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm {{
            color: {('#FFFFFF' if dark_mode else '#000000')} !important;
        }}
        
        textarea {{
            color: {('#FFFFFF' if dark_mode else '#000000')} !important;
            font-family: "Source Sans", sans-serif !important;
            font-size: 16px !important;
            line-height: 1.5 !important;
        }}
        
        /* Buton Stili */
        .stButton > button {{
            background: linear-gradient(90deg, var(--accent-color), var(--accent-hover)) !important;
            color: white !important;
            border-radius: 12px !important;
            border: none !important;
            padding: 0.5rem 2rem !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 12px var(--shadow-color) !important;
        }}


        
        /* Mesaj Balonları */
        .user-message {{
            background: {('#0F172A' if dark_mode else '#F1F5F9')};
            color: var(--text-primary);
            padding: 1rem;
            border-radius: 12px;
            margin: 0.5rem 0;
            box-shadow: 0 2px 4px var(--shadow-color);
            border: 1px solid var(--border-color);
        }}
        
        .bot-message {{
            background: {('#1E293B' if dark_mode else '#000000')};
            color: var(--text-label);
            padding: 1rem;
            border-radius: 12px;
            margin: 0.5rem 0;
            box-shadow: 0 2px 4px var(--shadow-color);
            border: 1px solid {('#2D3B4E' if dark_mode else '#000000')};
        }}
        
        /* Genel Metin Renkleri */
        .stMarkdown {{
            color: var(--text-primary) !important;
        }}
        
        .stMarkdown p {{
            color: var(--text-muted) !important;
        }}

        /* Streamlit emotion cache stil override */
        .st-emotion-cache-1j90q2q {{
            color: {('#FFFFFF' if dark_mode else '#000000')} !important;
        }}
        
        /* Checkbox Stili - Theme based */
        div[data-testid="stCheckbox"] label p,
        div[data-testid="stCheckbox"] label span,
        div.stCheckbox label p,
        div.stCheckbox label span {{
            color: {('#FFFFFF' if dark_mode else '#000000')} !important;
            font-weight: 500 !important;
            opacity: 1 !important;
        }}
        
        /* Form Elemanları */
        .stMarkdown, .stTextArea label, div[data-testid="stText"] {{
            color: var(--text-label) !important;
        }}
        
        /* Başlıklar */
        h1, h2, h3, h4, h5, h6 {{
            color: var(--text-primary) !important;
        }}
        
        /* Divider Stili */
        hr {{
            border-color: var(--border-color) !important;
        }}
        </style>
        """, unsafe_allow_html=True)

    # Logo ve başlığı container içinde göster
    try:
        logo_base64 = get_base64_from_file('logo.png')
    except:
        logo_base64 = None  # Continue without logo if file is missing
    if logo_base64:
        st.markdown(f"""
            <div class="header-container">
                <img src="data:image/png;base64,{logo_base64}" class="header-logo" alt="Civbot Logo">
                <h1 class="header-title">Civbot - Hafıza ve Günün Cümlesi Asistanı</h1>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.title("Civbot - Hafıza ve Günün Cümlesi Asistanı")
        
    # Günün sözünü özel stil ile göster
    daily_quote = get_daily_quote()
    st.markdown(f'<div class="daily-quote">{daily_quote} 💫</div>', unsafe_allow_html=True)

    # API anahtarı kontrolü
    if not GEMINI_API_KEY:
        st.warning("🔑 Google Gemini API anahtarı gerekli")
        st.markdown("""
        1. [Google AI Studio](https://makersuite.google.com/app/apikey) sayfasına gidin
        2. API anahtarı oluşturun
        3. Anahtarı aşağıya yapıştırın
        """)
        key = st.text_input("Google Gemini API Key", type="password")
        if key:
            if configure_api(key):
                GEMINI_API_KEY = key
                st.success("✅ API anahtarı başarıyla yapılandırıldı!")
                st.rerun()  # Sayfayı yenile
            else:
                st.error("❌ API anahtarı geçersiz veya bir hata oluştu")

    memory = load_memory()

    # Konuşma geçmişini session state'de tut
    if "conversation_preview" not in st.session_state:
        st.session_state["conversation_preview"] = memory[-6:]

    st.markdown("---")

    user_input = st.text_area("Mesajınızı yazın:", height=120, key="user_input")
    
    # Custom CSS for the button alignment
    st.markdown("""
    <style>
    div.stButton > button {
        margin-left: 0;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if st.button("Gönder"):
            if not user_input or not user_input.strip():
                st.warning("Lütfen bir mesaj yazın.")
            else:
                try:
                    with st.spinner("Cevap alınıyor…"):
                        answer = ask_gemini(user_input.strip(), memory)

                    # Hafızaya hem kullanıcı hem Civbot mesajını kaydet
                    ts = datetime.utcnow().isoformat()
                    memory.append({"role": "user", "content": user_input.strip(), "ts": ts})
                    memory.append({"role": "assistant", "content": answer, "ts": ts})
                    save_memory(memory)

                    # Güncel preview'ı güncelle
                    st.session_state["conversation_preview"].append({"role": "user", "content": user_input.strip()})
                    st.session_state["conversation_preview"].append({"role": "assistant", "content": answer})
                    # Keep preview small
                    st.session_state["conversation_preview"] = st.session_state["conversation_preview"][-6:]

                    st.markdown(f'<div class="bot-message">🤖 {answer}</div>', unsafe_allow_html=True)
                except RuntimeError as e:
                    st.error(str(e))
                except Exception as e:
                    st.error(f"Gemini API isteği sırasında bir hata oluştu: {e}")

    # Hafızayı gösterme seçeneği
    st.markdown("""
    <style>
    .memory-entry {{
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        background: #1E293B;
        border: 1px solid #2D3B4E;
        box-shadow: 0 2px 4px var(--shadow-color);
    }}
    .memory-entry .role {{
        font-weight: 600;
        color: #00AEEF;
        display: inline-block;
        margin-bottom: 0.5rem;
    }}
    .memory-entry .timestamp {{
        font-size: 0.8em;
        color: #94A3B8;
        margin-left: 0.5rem;
    }}
    .memory-entry .content {{
        color: #FFFFFF;
        margin-top: 0.5rem;
        line-height: 1.5;
    }}
    /* Default styles */
    .stTextArea textarea {
        color: #00AEEF !important;
    }
    
    /* Checkbox styles */
    div[data-testid="stCheckbox"] label {
        color: var(--accent-color) !important;
    }}

    </style>
    """, unsafe_allow_html=True)
    
    if st.checkbox("Hafızayı Göster"):
        st.subheader("📚 Hafıza Geçmişi (tüm kayıtlar)")
        if not memory:
            st.info("Hafıza boş. Henüz kayıt yok.")
        else:
            for entry in memory:
                role = "👤 Kullanıcı" if entry.get("role") == "user" else "🤖 Civbot"
                ts = entry.get("ts", "")
                ts_display = f"<span class='timestamp'>({ts})</span>" if ts else ""
                content = entry.get("content", "")
                
                st.markdown(f"""
                <div class='memory-entry'>
                    <span class='role'>{role}</span> {ts_display}
                    <div class='content'>{content}</div>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()



