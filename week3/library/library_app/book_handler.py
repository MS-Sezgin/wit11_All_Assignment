from library_app.file_handler import read_file, write_file,csv_creater,csv_reader
from library_app.api import lookup_book
def add_book(kitaplar):
    baslik = input("Title: ")
    yazar,yil=lookup_book(baslik)
    if yazar is None:
        yazar = input("Author: ")
        while True:
            yil = input("Year: ")
            try:
                yil = int(yil)
                break
            except ValueError:
                print("Girdiğiniz değer bir sayi olmali, yeniden giriş yapin")
    else:
        print(f"Otomatik bulundu: {yazar}, {yil}")
    tur = input("Genre: ")
    kitaplar.append({"title": baslik,"author": yazar,"year": yil,"genre": tur})
    write_file("data/library.json",kitaplar)
    ##return kitaplar##Ben bunu return etmesemde parametre olarak gelen liste değişir. Yani geldiği yerdeki liste değişir

def print_book(kitaplar):
    if not kitaplar:
        print("Kitap listesi boş")
    else:
        print(f"{'Title':<40} | {'Author':<20} | {'Year':<6} | {'Genre':<15}")
        print("-" * 70)
        for kitap in kitaplar:
            print(f"{kitap['title']:40} | {kitap['author']:<20} | {kitap['year']:<6} | {kitap['genre']:<15}")  

def search_book(kitaplar):
    aranan_kelime=input("aramak istediğiniz kitabin adini girin")
    search_list=list(filter(lambda x:aranan_kelime.lower() in x["title"].lower() or aranan_kelime.lower() in x["author"].lower(),kitaplar))
    return search_list

def del_book(kitaplar):
    baslik = input("Silinecek kitabin adini girin: ")
    bulundu = False
    for kitap in kitaplar:
        if kitap["title"].lower() == baslik.lower():
            kitaplar.remove(kitap)
            write_file("data/library.json",kitaplar)
            bulundu = True
            break
    if not bulundu:
        print("Böyle bir kitap bulunamadi.")