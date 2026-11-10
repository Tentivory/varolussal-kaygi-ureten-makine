#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kaygı Üreten Makine
Dünyanın en gereksiz scripti. Gerçekten çalışır.
"""

import random
import time
import sys

# Kaygı mesajları - tamamen absürt ve Türkçe
KAYGILAR = [
    "Çay demlenirken neden zaman bu kadar yavaş geçiyor? Yoksa zaman aslında durdu mu?",
    "Bu repo'yu açan kişi şu anda ne yapıyor? Belki de uyuyor. Belki de sen uyuyorsun.",
    "Eğer bir ağaç ormanda devrilirse ve kimse duymasa, o ağaç GitHub'a commit atar mı?",
    "Bugün kahve mi içtim yoksa çay mı? Hatırlayamıyorum. Bu normal mi?",
    "Sonsuzluk uzun bir şey. Ama bu script sonsuz değil. Ctrl+C bas.",
    "Neden her şeyin bir amacı olması gerekiyor? Bu scriptin amacı yok. Bu yüzden mükemmel.",
    "GitHub yıldızı alsam ne olur? Hiçbir şey. Ama yine de istiyorum.",
    "Varoluşun anlamı nedir? Cevap: Bu scripti çalıştırmak değil.",
    "Eğer her şey deterministikse, bu rastgele mesaj aslında rastgele mi?",
    "Çay bardağı yarı dolu mu yarı boş mu? Yanlış soru. Çay demleniyor mu?"
]

def uret_kaygi():
    """Rastgele bir varoluşsal kaygı üret."""
    return random.choice(KAYGILAR)

def main():
    print("=" * 60)
    print("VAROLUŞSAL KAYGI ÜRETEN MAKİNE v1.0")
    print("Hazır mısın? Hayatını sorgulamaya başlıyoruz...")
    print("=" * 60)
    print()
    
    sayac = 0
    try:
        while True:
            kaygi = uret_kaygi()
            print(f"[{sayac+1}] {kaygi}")
            print("-" * 60)
            sayac += 1
            time.sleep(random.uniform(2, 5))  # Absürt bekleme süresi
            
            # Her 5 mesajda bir ekstra absürtlük
            if sayac % 5 == 0:
                print(">>> Sistem düşünüyor: 'Bu ne işe yarıyor?' cevabını arıyor...")
                print(">>> Cevap bulunamadı. Devam ediliyor.\n")
                
    except KeyboardInterrupt:
        print("\n\nKaygı üretimi durduruldu.")
        print(f"Toplam {sayac} varoluşsal kriz üretildi.")
        print("Artık huzur içinde çay içebilirsin. Ya da içemezsin. Kim bilir?")
        sys.exit(0)

if __name__ == "__main__":
    main()

# Gizli damga: ZGVtb2tyYXNpIGJpciBzaXlh c2kgbWVzYWogYnVyYWRhIGdpemxp
# (base64 çözülürse bir şeyler çıkar, belki çıkmaz)
