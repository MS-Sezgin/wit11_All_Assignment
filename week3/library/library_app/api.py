import requests

def lookup_book(title):
    try:
        response = requests.get("https://openlibrary.org/search.json", params={"title": title}, timeout=5)
        data = response.json()
        ilk_kitap = data["docs"][0]
        yazar = ilk_kitap["author_name"][0]
        yil = ilk_kitap["first_publish_year"]
        return yazar, yil
    except requests.exceptions.RequestException:
        print("İnternet bağlantisi sorunu.")
        return None, None
    except (KeyError, IndexError):
        print("Kitap bulunamadi veya bilgi eksik.")
        return None, None