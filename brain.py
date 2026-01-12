import time

def get_jarvis_response(messages):
    """
    Bu fonksiyon şu an simülasyon yapıyor.
    İleride buraya OpenAI veya LangChain kodlarını bağlayabilirsin.
    """
    last_user_message = messages[-1]["content"].lower()
    
    # Basit bir cevap simülasyonu
    time.sleep(1) # Yapay zeka düşünüyor efekti
    
    if "merhaba" in last_user_message:
        return "Merhaba efendim. Sistemler hazır. Size nasıl yardımcı olabilirim?"
    elif "stok" in last_user_message:
        return "Global stok verilerine erişiyorum... Şu anda depoda 12 kritik ürün tespit edildi."
    elif "finans" in last_user_message:
        return "Finansal raporlar derleniyor. Bugünkü harcama limitiniz %15 oranında altında."
    else:
        return "Bu komutu işleme aldım. Analiz yapıyorum, lütfen bekleyin..."
