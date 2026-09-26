from library_app.file_handler import read_file, write_file,csv_creater,csv_reader
from library_app.book_handler import add_book, print_book,search_book,del_book
kitaplar=read_file("data/library.json")
print(kitaplar)

def main_menu():
    print("""
            1. Kitap ekle
            2. Tüm kitaplari görüntüle
            3. Kitap ara
            4. Kitap sil
            5. CSV'ye aktar
            6. CSV'den içe aktar
            7. Exit
            """)
    secim=input("Bir secim yapiniz")
    try:
        secim=int(secim)
        return secim
    except ValueError:
        print("lütfen integer bir deger girin")
    return secim

while True:
    secim=main_menu()
    if secim==1:
        add_book(kitaplar)
    elif secim==2:
        print_book(kitaplar)
    elif secim==3:
        print_book(search_book(kitaplar))
    elif secim==4:
        del_book(kitaplar)
    elif secim==5:
        csv_creater("data/library.csv",kitaplar)
    elif secim==6:
        kitaplar.extend(csv_reader("data/library.csv"))
        write_file("data/library.json",kitaplar)
    elif secim==7:
        break
    