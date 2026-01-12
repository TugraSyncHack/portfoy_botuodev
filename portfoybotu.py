print("🤖 Portföy Botuna Hoş Geldin!")
print("Yazabileceğin komutlar:")
print("- hakkimda")
print("- projeler")
print("- iletisim")
print("- cikis")

while True:
    komut = input("\n👉 Bir komut yaz: ").lower()

    if komut == "hakkimda":
        print("\n👋 Merhaba!")
        print("Ben kodlama kursunda eğitim alan bir öğrenciyim.")
        print("Python öğreniyorum ve projeler geliştiriyorum 🚀")

    elif komut == "projeler":
        print("\n📂 Projelerim:")
        print("- Portföy Botu 🤖")
        print("- Basit Hesap Makinesi 🧮")
        print("- Python Oyun Denemeleri 🎮")

    elif komut == "iletisim":
        print("\n📬 İletişim:")
        print("GitHub: https://github.com/yazmasamdaolur")
        print("E-posta: tugrakiss@gmail.com")

    elif komut == "cikis":
        print("\n👋 Bot kapatılıyor. Görüşürüz!")
        break

    else:
        print("\n❌ Bu komutu anlamadım. Tekrar dene.")
