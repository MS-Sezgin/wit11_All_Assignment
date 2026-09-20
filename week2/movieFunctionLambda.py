from functools import reduce

####### Değişkenlerimiz
filmler = [
    {
        "baslik": "Yıldızlararası",
        "turler": {"Bilim Kurgu", "Macera"},
        "seanslar": [
            {"tarih": "2026-09-20", "saat": "14:00", "salon_numarasi": 1,
             "koltuk_sayisi": 100, "kalan_koltuk": 45, "fiyat": 120, "satilan_bilet": 55},
            {"tarih": "2026-09-20", "saat": "19:30", "salon_numarasi": 3,
             "koltuk_sayisi": 80, "kalan_koltuk": 12, "fiyat": 150, "satilan_bilet": 68},
            {"tarih": "2026-09-21", "saat": "22:00", "salon_numarasi": 1,
             "koltuk_sayisi": 100, "kalan_koltuk": 90, "fiyat": 120, "satilan_bilet": 10}
        ]
    },
    {
        "baslik": "Gülümseme",
        "turler": {"Korku", "Gerilim"},
        "seanslar": [
            {"tarih": "2026-09-21", "saat": "21:00", "salon_numarasi": 2,
             "koltuk_sayisi": 60, "kalan_koltuk": 60, "fiyat": 100, "satilan_bilet": 0}
        ]
    },
    {
        "baslik": "Aşk Tesadüfleri Sever",
        "turler": {"Romantik", "Komedi"},
        "seanslar": [
            {"tarih": "2026-09-22", "saat": "17:00", "salon_numarasi": 4,
             "koltuk_sayisi": 50, "kalan_koltuk": 0, "fiyat": 90, "satilan_bilet": 50},
            {"tarih": "2026-09-23", "saat": "20:00", "salon_numarasi": 1,
             "koltuk_sayisi": 100, "kalan_koltuk": 30, "fiyat": 110, "satilan_bilet": 70}
        ]
    },
    {
        "baslik": "Ejderha Avcısı",
        "turler": {"Aksiyon", "Macera", "Fantastik"},
        "seanslar": [
            {"tarih": "2026-09-24", "saat": "15:30", "salon_numarasi": 5,
             "koltuk_sayisi": 120, "kalan_koltuk": 75, "fiyat": 130, "satilan_bilet": 45}
        ]
    },
    {
        "baslik": "Sessiz Ev",
        "turler": {"Korku"},
        "seanslar": [
            {"tarih": "2026-09-25", "saat": "22:00", "salon_numarasi": 2,
             "koltuk_sayisi": 60, "kalan_koltuk": 5, "fiyat": 85, "satilan_bilet": 55},
            {"tarih": "2026-09-26", "saat": "23:00", "salon_numarasi": 2,
             "koltuk_sayisi": 60, "kalan_koltuk": 60, "fiyat": 85, "satilan_bilet": 0}
        ]
    },
    {
        "baslik": "Uzay Kasabi",
        "turler": {"Bilim Kurgu", "Komedi"},
        "seanslar": [
            {"tarih": "2026-09-27", "saat": "18:00", "salon_numarasi": 3,
             "koltuk_sayisi": 80, "kalan_koltuk": 80, "fiyat": 95, "satilan_bilet": 0}
        ]
    },
    {
        "baslik": "Son Nefes",
        "turler": {"Aksiyon", "Gerilim"},
        "seanslar": [
            {"tarih": "2026-09-28", "saat": "16:00", "salon_numarasi": 4,
             "koltuk_sayisi": 50, "kalan_koltuk": 20, "fiyat": 105, "satilan_bilet": 30},
            {"tarih": "2026-09-28", "saat": "21:30", "salon_numarasi": 4,
             "koltuk_sayisi": 50, "kalan_koltuk": 0, "fiyat": 125, "satilan_bilet": 50}
        ]
    },
    {
        "baslik": "Küçük Şeyler",
        "turler": {"Drama"},
        "seanslar": [
            {"tarih": "2026-09-29", "saat": "19:00", "salon_numarasi": 5,
             "koltuk_sayisi": 120, "kalan_koltuk": 100, "fiyat": 75, "satilan_bilet": 20}
        ]
    },
    {
        "baslik": "Kahkaha Kulübü",
        "turler": {"Komedi"},
        "seanslar": [
            {"tarih": "2026-09-30", "saat": "20:30", "salon_numarasi": 3,
             "koltuk_sayisi": 80, "kalan_koltuk": 15, "fiyat": 80, "satilan_bilet": 65}
        ]
    },
    {
        "baslik": "Derin Sular",
        "turler": {"Gerilim", "Dram"},
        "seanslar": [
            {"tarih": "2026-10-01", "saat": "18:30", "salon_numarasi": 2,
             "koltuk_sayisi": 60, "kalan_koltuk": 60, "fiyat": 100, "satilan_bilet": 0}
        ]
    }
]

snack_menu = {
    "Patlamis misir (Large)": 6.0,
    "Patlamis misir (Small)": 4.0,
    "Kola": 3.5,
    "Fanta": 3.5,
    "Nachos": 8.5,
    "Su": 2.0,
    "Cikolata": 5.0,
    "Dondurma": 7.0,
    "Hot Dog": 9.5
}

müsteriler = {
    "Ahmet Yilmaz": [
        {"film":"Yıldızlararası","seans":"14:00","koltuk_sayisi":2,
         "atistirmaliklar":{"Kola":2,"Patlamis misir (Large)":1},"toplam_tutar":275.19},
        {"film":"Ejderha Avcısı","seans":"15:30","koltuk_sayisi":1,
         "atistirmaliklar":{},"toplam_tutar":137.86},
        {"film":"Son Nefes","seans":"16:00","koltuk_sayisi":3,
         "atistirmaliklar":{"Nachos":2,"Su":3},"toplam_tutar":365.40}
    ],
    "Zeynep Kaya": [
        {"film":"Aşk Tesadüfleri Sever","seans":"20:00","koltuk_sayisi":3,
         "atistirmaliklar":{"Nachos":1,"Su":3},"toplam_tutar":382.15},
        {"film":"Kahkaha Kulübü","seans":"20:30","koltuk_sayisi":2,
         "atistirmaliklar":{"Dondurma":2,"Cikolata":1},"toplam_tutar":183.27}
    ],
    "Mehmet Demir": [],
    "Elif Sahin": [
        {"film":"Sessiz Ev","seans":"22:00","koltuk_sayisi":4,
         "atistirmaliklar":{"Patlamis misir (Large)":2,"Kola":4,"Hot Dog":1},"toplam_tutar":471.83}
    ],
    "Can Ozturk": [
        {"film":"Yıldızlararası","seans":"19:30","koltuk_sayisi":1,
         "atistirmaliklar":{"Fanta":1},"toplam_tutar":163.35},
        {"film":"Aşk Tesadüfleri Sever","seans":"17:00","koltuk_sayisi":2,
         "atistirmaliklar":{},"toplam_tutar":190.19},
        {"film":"Uzay Kasabi","seans":"18:00","koltuk_sayisi":0,
         "atistirmaliklar":{},"toplam_tutar":0}
    ]
}
#######


####### Fonksiyonlar #######

def film_bul(filmler, baslik):
    sonuc=list(filter(lambda film: film["baslik"]==baslik, filmler))
    if len(sonuc)==0:
        return None
    return sonuc[0]


def tur_ile_ara(filmler, aranan_tur):
    return list(filter(lambda film: aranan_tur in film["turler"], filmler))


def fiyat_ile_ara(filmler, max_fiyat):
    return list(filter(lambda film: any(map(lambda seans: seans["fiyat"]<=max_fiyat, film["seanslar"])), filmler))


def film_ekle(filmler):
    yeni_baslik = input("Filmin adini girin: ")

    turler=set()
    while True:
        turler.add(input("Bir tur girin (ornek: Komedi): "))
        devamMi=input("Baska tur eklemek ister misiniz? (e/h): ")
        if devamMi!="e":
            break

    seans=[]
    seansTarih=input("Seans tarihini girin (YYYY-AA-GG formatinda, ornek: 2026-09-20): ")
    seansSaat=input("Seans saatini girin (SS:DD formatinda, ornek: 19:30): ")
    seansSalon=input("Seans salon numarasini girin (ornek: 3): ")
    seanskoltuk=int(input("Seans toplam koltuk sayisini girin (sayi, ornek: 80): "))
    seansfiyat=int(input("Seans koltuk fiyatini girin (TL, sayi, ornek: 120): "))
    seans.append({"tarih":seansTarih,"saat":seansSaat,"salon_numarasi":seansSalon,"koltuk_sayisi":seanskoltuk,
                  "kalan_koltuk":seanskoltuk,"fiyat":seansfiyat,"satilan_bilet":0})
    filmler.append({"baslik":yeni_baslik,"turler":turler,"seanslar":seans})


def seanslari_yazdir(film):
    sayac=0
    for seans in film["seanslar"]:
        print(sayac, "-", seans["tarih"], seans["saat"], "Salon:", seans["salon_numarasi"],
              "Kalan Koltuk:", seans["kalan_koltuk"], "Fiyat:", seans["fiyat"])
        sayac=sayac+1


def koltuk_sat(seans, istenen_koltuk):
    if istenen_koltuk>seans["kalan_koltuk"]:
        return False
    seans["kalan_koltuk"]=seans["kalan_koltuk"]-istenen_koltuk
    seans["satilan_bilet"]=seans["satilan_bilet"]+istenen_koltuk
    return True


def atistirmalik_siparisi_al(snack_menu):
    siparis_atistirmaliklari={}
    while True:
        devamMi=input("Atistirmalik eklemek ister misiniz? (e/h): ")
        if devamMi=="e":
            print("Menü:")
            for urun in snack_menu:
                print("-", urun, ":", snack_menu[urun], "TL")

            urun_adi=input("Eklemek istediginiz urunu menudeki gibi tam yazin: ")

            if urun_adi not in snack_menu:
                print(urun_adi, "menüde bulunamadı.")
            else:
                miktar=int(input("Kaç adet istiyorsunuz (sayi, ornek: 2): "))
                if miktar<=0:
                    print("Miktar 0'dan büyük olmalı.")
                else:
                    if urun_adi in siparis_atistirmaliklari:
                        siparis_atistirmaliklari[urun_adi]=siparis_atistirmaliklari[urun_adi]+miktar
                    else:
                        siparis_atistirmaliklari[urun_adi]=miktar
                    print(urun_adi, "x", miktar, "eklendi.")
        elif devamMi=="h":
            break
        else:
            print("Geçersiz giriş, 'e' veya 'h' yazın.")
    return siparis_atistirmaliklari


def atistirmalik_tutari_hesapla(snack_menu, siparis_atistirmaliklari):
    return sum(map(lambda urun: snack_menu[urun]*siparis_atistirmaliklari[urun], siparis_atistirmaliklari))


def ucretleri_uygula(tutar, oranlar):
    if len(oranlar)==0:
        return tutar
    else:
        yeniTutar=tutar*(1+oranlar[0])
        kalanOranlar=oranlar[1:]
        return ucretleri_uygula(yeniTutar, kalanOranlar)


def fis_yazdir(musteriAdi, film, seans, istenenKoltuk, biletTutari, siparis_atistirmaliklari, snack_menu, subtotal, toplamTutar):
    print("========== FİŞ ==========")
    print("Müşteri:", musteriAdi)
    print("Film:", film["baslik"], "-", seans["saat"])
    print("Bilet (", istenenKoltuk, "x", seans["fiyat"], "TL ) =", biletTutari, "TL")
    for urun in siparis_atistirmaliklari:
        print(urun, "x", siparis_atistirmaliklari[urun], "=", snack_menu[urun]*siparis_atistirmaliklari[urun], "TL")
    print("--------------------------")
    print("Ara Toplam:", round(subtotal,2), "TL")
    print("Toplam (ücretler dahil):", round(toplamTutar,2), "TL")
    print("==========================")


def siparisi_kaydet(müsteriler, musteriAdi, film, seans, istenenKoltuk, siparis_atistirmaliklari, toplamTutar):
    yeniSiparis={"film":film["baslik"],"seans":seans["saat"],
                 "koltuk_sayisi":istenenKoltuk,"atistirmaliklar":siparis_atistirmaliklari,
                 "toplam_tutar":round(toplamTutar,2)}
    müsteriler[musteriAdi].append(yeniSiparis)


def snack_menu_guncelle(snack_menu):
    print("Şu anki menü:")
    for urun in snack_menu:
        print("-", urun, ":", snack_menu[urun], "TL")

    islem=input("Urun eklemek mi istiyorsunuz, cikarmak mi? (ekle/cikar): ")

    if islem=="ekle":
        urun_adi=input("Eklemek istediginiz urunun adini girin: ")
        urun_fiyati=float(input("Urunun fiyatini girin (TL, ondalikli sayi, ornek: 6.5): "))
        snack_menu[urun_adi]=urun_fiyati
        print(urun_adi, "menüye eklendi.", urun_fiyati, "TL")
    elif islem=="cikar":
        urun_adi=input("Cikarmak istediginiz urunun adini menudeki gibi tam yazin: ")
        if urun_adi in snack_menu:
            del snack_menu[urun_adi]
            print(urun_adi, "menüden çıkarıldı.")
        else:
            print(urun_adi, "menüde bulunamadı.")
    else:
        print("Geçersiz giriş, 'ekle' veya 'cikar' yazın.")


def musteri_gecmisi_goster(müsteriler, musteriAdi):
    if musteriAdi not in müsteriler:
        print(musteriAdi, "adinda bir musteri bulunamadi.")
    elif len(müsteriler[musteriAdi])==0:
        print(musteriAdi, "icin henuz bir siparis yok.")
    else:
        print(musteriAdi, "musterisinin siparis gecmisi:")
        for siparis in müsteriler[musteriAdi]:
            print("-", siparis["film"], "(", siparis["seans"], ") -", siparis["koltuk_sayisi"], "bilet -", siparis["toplam_tutar"], "TL")


def populerlik_raporu(filmler):
    print("========== POPULERLIK RAPORU ==========")

    siralama=[]
    for film in filmler:
        toplamBilet=sum(map(lambda seans: seans["satilan_bilet"], film["seanslar"]))
        siralama.append((film["baslik"], toplamBilet))

    siralama=sorted(siralama, key=lambda kayit: kayit[1], reverse=True)

    sira=1
    for kayit in siralama:
        print(sira, "-", kayit[0], ":", kayit[1], "bilet satildi")
        sira=sira+1

    genelToplam=reduce(lambda toplam, kayit: toplam+kayit[1], siralama, 0)
    print("--------------------------")
    print("Tum filmler toplam satilan bilet:", genelToplam)
    print("=========================================")


def filmleri_listele(filmler):
    print("========== FILMLER ==========")
    for film in filmler:
        turler_metni=", ".join(film["turler"])
        print(film["baslik"], "(", turler_metni, ")")
        for seans in film["seanslar"]:
            print("   -", seans["tarih"], seans["saat"], "| Salon:", seans["salon_numarasi"],
                  "| Fiyat:", seans["fiyat"], "TL | Kalan Koltuk:", seans["kalan_koltuk"])
        print("------------------------------")
    print("==============================")
#############################


while True:

    print("""
        1-Film Ekle
        2-Filmleri Listele
        3-Film Ara
        4-Koltuk Sat
        5-Atistirmalik Menüsünü Güncelle
        6-Musteri Gecmisi
        7-Populerlik Raporu
        9-Exit      
        """)
    secim=int(input("Bir secim yapin (1, 2, 3, 4, 5, 6, 7 veya 9): "))


    if secim==1:
        film_ekle(filmler)

    elif secim==2:
        filmleri_listele(filmler)

    elif secim==3:
        print("""
                     1-Filmleri Türüne Göre Listele
                     2-Filmleri Max Bilet Fiyatina Göre Listele
                     """)
        secim2=int(input("Secim yapin (1 veya 2): "))
        if secim2==1:
            arananTur=input("Aramak istediginiz filmin turunu girin (ornek: Komedi): ")
            search=tur_ile_ara(filmler,arananTur)
            if len(search)==0:
                print(arananTur, "turunde su an bir film bulunmuyor.")
            else:
                for i in search:
                    print(i["baslik"])
        if secim2==2:
            maxFiyat=int(input("Aramak istediginiz filmin max fiyatini girin (TL, sayi, ornek: 100): "))
            search=fiyat_ile_ara(filmler,maxFiyat)
            if len(search)==0:
                print(maxFiyat, "TL altinda gosterimde bir film bulunmuyor.")
            else:
                for i in search:
                    print(i["baslik"])

    elif secim==4:
        musteriAdi=input("Bilet almak isteyen musterinin adini girin: ")
        if musteriAdi not in müsteriler:
            müsteriler[musteriAdi]=[]

        filmAdi_BiletAl=input("Bilet almak istediginiz filmin adini listedeki gibi tam yazin: ")
        secilenFilm=film_bul(filmler, filmAdi_BiletAl)

        if secilenFilm==None:
            print("Böyle bir film bulunamadı.")
        else:
            print(secilenFilm["baslik"], "için gösterim saatleri:")
            seanslari_yazdir(secilenFilm)

            seansSecimi=int(input("Seans numarasini girin (yukaridaki listeden bir sayi, ornek: 0): "))

            if seansSecimi<0 or seansSecimi>=len(secilenFilm["seanslar"]):
                print("Geçersiz seans numarası.")
            else:
                secilenSeans=secilenFilm["seanslar"][seansSecimi]
                istenenKoltuk=int(input("Kaç koltuk almak istiyorsunuz (sayi, ornek: 2): "))

                satisBasarili=koltuk_sat(secilenSeans, istenenKoltuk)

                if not satisBasarili:
                    print("Yeterli koltuk yok! Kalan koltuk sayısı:", secilenSeans["kalan_koltuk"])
                else:
                    biletTutari=istenenKoltuk*secilenSeans["fiyat"]
                    print("Koltuk satışı başarılı:", istenenKoltuk, "koltuk.")

                    siparis_atistirmaliklari=atistirmalik_siparisi_al(snack_menu)
                    atistirmalikTutari=atistirmalik_tutari_hesapla(snack_menu, siparis_atistirmaliklari)

                    subtotal=biletTutari+atistirmalikTutari
                    toplamTutar=ucretleri_uygula(subtotal)

                    fis_yazdir(musteriAdi, secilenFilm, secilenSeans, istenenKoltuk, biletTutari,
                               siparis_atistirmaliklari, snack_menu, subtotal, toplamTutar)

                    siparisi_kaydet(müsteriler, musteriAdi, secilenFilm, secilenSeans, istenenKoltuk,
                                     siparis_atistirmaliklari, toplamTutar)

    elif secim==5:
        snack_menu_guncelle(snack_menu)

    elif secim==6:
        musteriAdi=input("Gecmisini gormek istediginiz musterinin adini girin: ")
        musteri_gecmisi_goster(müsteriler, musteriAdi)

    elif secim==7:
        populerlik_raporu(filmler)

    elif secim==9:
        break