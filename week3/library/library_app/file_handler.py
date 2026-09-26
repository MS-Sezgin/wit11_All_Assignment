import json
import csv
import os

def read_file(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        print("Dosya bulunamadi, boş kütüphane ile başliyorum.")
        return []
    try:
        with open(dosya_yolu, "r") as f:
            kitap_listesi = json.load(f)
    except json.JSONDecodeError:
        print("Dosya bozuk!")
        kitap_listesi = []
    return kitap_listesi

def write_file(dosya_yolu,kitap_listesi):
    with open(dosya_yolu, "w") as f:
        json.dump(kitap_listesi, f, indent=4)

def csv_creater(dosya_yolu,kitap_listesi):
        with open(dosya_yolu, "w", newline="") as f:
            alan_adlari = ["title", "author", "year", "genre"]
            yazici = csv.DictWriter(f, fieldnames=alan_adlari)
            yazici.writeheader()
            for kitap in kitap_listesi:
                yazici.writerow(kitap)

def csv_reader(dosya_yolu):
    kitap_listesi = []
    try:
        with open(dosya_yolu, "r") as f:
            okuyucu = csv.DictReader(f)
            for satir in okuyucu:
                kitap_listesi.append(satir)
    except FileNotFoundError:
        print("CSV dosyasi bulunamadi!")
    return kitap_listesi