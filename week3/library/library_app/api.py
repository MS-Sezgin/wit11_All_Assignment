import requests

response = requests.get("https://openlibrary.org/search.json", params={"title": "Dune"})
data = response.json()
ilk_kitap = data["docs"][0]
yazar = ilk_kitap["author_name"][0]
print(yazar)