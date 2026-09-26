def kitap_ekle(kitaplar):
    kitap_adi = input("Title: ")
    yazar = input("Author: ")
    yil = input("Year: ")
    tur = input("Genre: ")
    kitaplar.append({"title": kitap_adi,"author": yazar,"year": yil,"genre": tur})
    print(kitaplar)

def kitap_yazdir(kitaplar):
    print(f"{'Title':<20} | {'Author':<20} | {'Year':<6} | {'Genre':<15}")
    print("-" * 70)
    for kitap in kitaplar:
        print(f"{kitap['title']:<20} | {kitap['author']:<20} | {kitap['year']:<6} | {kitap['genre']:<15}")

def kitap_ara(kitaplar):
    aranacak_kelime=input("aramak istediğiniz kitabin adini girin")
    newList=list(filter(lambda x:aranacak_kelime.lower() in x["title"].lower() ,kitaplar))
    kitap_yazdir(newList)
    #search_list=list(filter(lambda x:aranacak_kelime.lower() in x["title"].lower() or aranacak_kelime.lower() in x["author"].lower(),kitaplar))

