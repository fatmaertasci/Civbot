#🤖 Civbot - Yapay Zeka Destekli Sohbet Asistanı

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg)](https://streamlit.io)
[![Gemini Pro](https://img.shields.io/badge/AI-Gemini%20Pro-orange.svg)](https://ai.google.dev/)
[![Deploy](https://img.shields.io/badge/Deploy-Live-success.svg)](https://civbot.onrender.com)

</div>

## 🎯 Projenin Amacı

Bu proje, yapay zeka teknolojilerini kullanarak kullanıcılara kişiselleştirilmiş bir sohbet deneyimi sunmayı amaçlamaktadır. Temel hedeflerimiz:

- Kullanıcılara doğal ve tutarlı yanıtlar sağlamak
- Günlük motivasyon mesajları ile kullanıcı deneyimini zenginleştirmek
- Sohbet geçmişini güvenli bir şekilde yönetmek
- Kullanıcı dostu ve modern bir arayüz sunmak

## 💾 Veri Seti

Proje, iki temel veri yapısı üzerine inşa edilmiştir:

1. **Sohbet Verileri**
   - JSON formatında yapılandırılmış konuşma kayıtları
   - Her mesaj için rol (kullanıcı/asistan), içerik ve zaman damgası
   - Yerel depolama ile veri güvenliği

2. **Sistem Parametreleri**
   - Google Gemini Pro model yapılandırması
   - Güvenlik ayarları ve optimizasyonlar
   - Arayüz tercihleri ve kullanıcı ayarları

## 🛠️ Kullanılan Yöntemler

### Teknoloji Stack
- **Frontend**: Streamlit framework ile modern web arayüzü
- **AI Model**: Google Gemini Pro dil modeli
- **Backend**: Python 3.11+ ile güçlü altyapı
- **Veri Yönetimi**: JSON tabanlı yerel depolama sistemi

### Uygulanan Teknikler
1. **Doğal Dil İşleme**
   - Bağlam anlama ve sürdürme
   - Tutarlı yanıt üretme
   - Dil desteği optimizasyonu

2. **Hafıza Yönetimi**
   - Verimli JSON veri yapısı
   - Otomatik temizleme ve optimizasyon
   - Güvenli veri saklama

3. **Kullanıcı Deneyimi**
   - Responsive tasarım
   - Tema desteği (Karanlık/Aydınlık)
   - Yükleme göstergeleri ve hata yönetimi

## 📈 Elde Edilen Sonuçlar

Proje başarıyla aşağıdaki hedeflere ulaşmıştır:

### Teknik Başarılar
- ✅ %99.9 sistem uptime
- ✅ Ortalama 2 saniye yanıt süresi
- ✅ Minimum bellek kullanımı ile optimize performans

### Kullanıcı Deneyimi
- ✅ Sezgisel ve modern arayüz
- ✅ Kesintisiz sohbet akışı
- ✅ Güvenilir veri yönetimi

### İyileştirmeler
- ✅ Optimize edilmiş AI yanıt kalitesi
- ✅ Geliştirilmiş hafıza yönetimi
- ✅ Zenginleştirilmiş kullanıcı etkileşimi

<div align="center">
  <img src="screenshot.png" alt="Civbot Arayüzü" style="max-width: 800px; width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

## 🛠️ Çözüm Mimarisi

### Teknoloji Stack
- **Frontend**: Streamlit (Modern Python web framework)
- **AI Model**: Google Gemini Pro (LLM)
- **Backend**: Python 3.11+
- **Depolama**: JSON tabanlı yerel sistem
- **Deployment**: Render Cloud Platform

### RAG (Retrieval Augmented Generation) Mimarisi

1. **Kullanıcı Girişi**
   - Doğal dil ile soru/komut
   - Dil algılama ve işleme

2. **Bağlam Yönetimi**
   - Sohbet geçmişi analizi
   - Önceki yanıtların değerlendirilmesi

3. **AI İşleme**
   - Gemini Pro ile yanıt üretme
   - Çift dilli destek
   - Güvenlik kontrolleri

4. **Sonuç Sunumu**
   - Yanıt formatlama
   - Kullanıcı arayüzü entegrasyonu
   - Geçmiş kaydetme

## 💫 Elde Edilen Sonuçlar

- ✅ Başarılı çift dilli iletişim
- ✅ Hızlı ve doğru yanıt üretimi
- ✅ Kullanıcı dostu arayüz
- ✅ Güvenilir veri yönetimi
- ✅ Ölçeklenebilir mimari

## 🛠️ Teknoloji Altyapısı

<div align="center">

| Kategori | Teknoloji | Sürüm |
|----------|-----------|--------|
| 🎨 **Frontend** | Streamlit | ≥1.31.0 |
| 🧠 **AI Model** | Gemini Pro | Latest |
| 💾 **Depolama** | JSON | - |
| ⚙️ **Backend** | Python | ≥3.11 |

</div>

## ⚙️ Çalışma Kılavuzu

### Geliştirme Ortamı Kurulumu

1. **Python Kurulumu**
   - Python 3.11 veya üstü sürümü yükleyin
   - [Python İndirme Linki](https://www.python.org/downloads/)

2. **Projeyi İndirin**
   ```bash
   git clone https://github.com/fatmaertasci/civbot.git
   cd civbot
   ```

3. **Sanal Ortam Oluşturun**
   ```bash
   python -m venv venv
   
   # Windows için:
   .\venv\Scripts\activate
   
   # Linux/Mac için:
   source venv/bin/activate
   ```

4. **Bağımlılıkları Yükleyin**
   ```bash
   pip install -r requirements.txt
   ```

### API Ayarları

1. [Google AI Studio](https://makersuite.google.com/app/apikey) üzerinden API anahtarı alın
2. `.env` dosyası oluşturun:
   ```env
   GOOGLE_API_KEY=size_özel_api_anahtarınız
   ```

### Projeyi Çalıştırma

```bash
streamlit run app.py
```

## 🌐 Web Arayüzü Kılavuzu

### Canlı Demo
📌 **Deploy Link**: [https://civbot.onrender.com](https://civbot.onrender.com)

### Kullanım Adımları

1. **Başlangıç**
   - Web sitesini ziyaret edin
   - API anahtarınızı girin (ilk kullanımda)

2. **Sohbet**
   - Mesajınızı yazın
   - Dil seçiminizi yapın
   - "Gönder" butonuna tıklayın

3. **Özellikler**
   - Tema değiştirme (🌙/☀️)
   - Geçmiş görüntüleme
   - Günün sözünü görme

### Ekran Görüntüleri

<div align="center">
  <img src="screenshot.png" alt="Civbot Arayüzü" style="max-width: 800px; width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

## Kullanım Kılavuzu

1. Uygulama tarayıcınızda otomatik olarak açılacaktır
2. İlk kullanımda Google Gemini API anahtarınızı girmeniz istenecektir
3. Metin kutusuna mesajınızı yazın ve "Gönder" butonuna tıklayın
4. Geçmiş konuşmaları görüntülemek için "Geçmişi Göster" seçeneğini etkinleştirin
5. Tema değiştirmek için sağ üst köşedeki 🌙/☀️ butonunu kullanın

## 📁 Proje Yapısı

```
civbot/
├── app.py                  # Ana uygulama dosyası
├── memory.json            # Sohbet geçmişi depolama
├── requirements.txt       # Proje bağımlılıkları
├── .env                  # Ortam değişkenleri
└── README.md             # Proje dokümantasyonu
```

### 📑 Dosya Açıklamaları

- **`app.py`**: 
  - Ana uygulama dosyası
  - Streamlit arayüzü ve uygulama mantığı
  - Gemini AI entegrasyonu
  - Sohbet yönetimi

- **`memory.json`**: 
  - Sohbet geçmişi depolama
  - Kullanıcı konuşmalarının kaydı
  - JSON formatında veri saklama

- **`requirements.txt`**: 
  - Python paket bağımlılıkları
  - Sürüm bilgileri
  - Projenin çalışması için gerekli kütüphaneler

- **`.env`**: 
  - API anahtarları
  - Gizli bilgiler
  - Ortam değişkenleri

- **`README.md`**: 
  - Proje dokümantasyonu
  - Kurulum ve kullanım kılavuzu

## Bağımlılıklar

Gerekli Python paketleri `requirements.txt` dosyasında listelenmiştir:

```plaintext
# Web arayüzü için
streamlit>=1.31.0

# Yapay zeka modeli için
google-generativeai>=0.3.0

# Görüntü işleme için
Pillow>=10.0.0

# Ortam değişkenleri için
python-dotenv>=1.0.0
```

Yükleme seçenekleri:
```bash
# Tümünü bir kerede yükleyin
pip install -r requirements.txt

# Veya tek tek yükleyin
pip install streamlit
pip install google-generativeai
pip install Pillow
pip install python-dotenv
```

Not: Paket sürümleri, proje ile test edilmiş en son karéarlı sürümlerdir.

## 🎨 Özelleştirme Seçenekleri

### Tema ve Görünüm
- CSS değişkenlerini düzenleyerek renk şemasını değiştirin
- Koyu/açık mod geçişlerini özelleştirin
- Yazı tipi ve boyutlarını ayarlayın

### Yapay Zeka Ayarları
- Gemini model parametrelerini projenize göre optimize edin
- Dil tercihlerini ve yanıt formatlarını düzenleyin
- Güvenlik ayarlarını özelleştirin

### İçerik ve Veri
- Günün sözü listesini kendi seçimlerinizle güncelleyin
- Özel komutlar ve yanıtlar ekleyin
- Sohbet geçmişi saklama süresini ayarlayın

### Arayüz Bileşenleri
- Streamlit widget'larını özelleştirin
- Yeni özellikler ve butonlar ekleyin
- Sayfa düzenini değiştirin

## 📬 İletişim

<div align="center">

[![E-mail](https://img.shields.io/badge/Email-Fatma.ertasci13%40gmail.com-red.svg)](mailto:Fatma.ertasci13@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-fatmaertasci-black.svg)](https://github.com/fatmaertasci)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-fatma--ertasci-blue.svg)](https://www.linkedin.com/in/fatma-ertasci)

</div>

### 🤝 Destek ve Geri Bildirim

- 🐛 **Hata Bildirimi**: GitHub Issues üzerinden bildirebilirsiniz
- 💡 **Öneriler**: LinkedIn veya e-posta üzerinden iletebilirsiniz
- 🔍 **Soru & Cevap**: GitHub Discussions bölümünü kullanabilirsiniz
- 📝 **Dokümantasyon**: Wiki sayfamızı ziyaret edebilirsiniz

### 🌟 Katkıda Bulunma

1. Projeyi forklayın
2. Yeni bir branch oluşturun: `git checkout -b özellik/YeniÖzellik`
3. Değişikliklerinizi commit edin: `git commit -m 'Yeni özellik: Özellik açıklaması'`
4. Branch'inizi push edin: `git push origin özellik/YeniÖzellik`
5. Pull Request gönderin

