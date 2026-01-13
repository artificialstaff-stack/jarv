# views/login.py İÇİNDEKİ USERS SÖZLÜĞÜNÜ BUNUNLA DEĞİŞTİR:

USERS = {
    # SENARYO 1: Kurumsal Lojistik Firması
    "demo": {
        "pass": "1234",
        "name": "Ahmet Yılmaz",
        "brand": "Anatolia Home",
        "role": "CEO",
        "plan": "Enterprise",
        "avatar": "AY",
        "config": {
            "primary_color": "#3B82F6", # Mavi
            "dashboard_title": "Global Operasyon Merkezi",
            "show_modules": ["dashboard", "logistics", "inventory", "documents"]
        }
    },
    # SENARYO 2: Teknoloji Şirketi (Tesla Tarzı)
    "tech": {
        "pass": "1234",
        "name": "Elon M.",
        "brand": "Cyber Systems",
        "role": "CTO",
        "plan": "Unlimited",
        "avatar": "EM",
        "config": {
            "primary_color": "#D946EF", # Neon Mor/Pembe
            "dashboard_title": "Neural Command Interface",
            "show_modules": ["dashboard", "todo", "plan", "forms"]
        }
    },
    # SENARYO 3: Moda Markası (Gucci Tarzı)
    "fashion": {
        "pass": "1234",
        "name": "Bella H.",
        "brand": "Lusso Milano",
        "role": "Creative Dir.",
        "plan": "Pro",
        "avatar": "BH",
        "config": {
            "primary_color": "#10B981", # Zümrüt Yeşili
            "dashboard_title": "Atelier Management",
            "show_modules": ["inventory", "plan", "documents"]
        }
    }
}
