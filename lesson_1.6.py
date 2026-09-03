"""

✅ Project 6: Mini Library Management System
Practice dictionaries, sets, loops, and string methods.

Library dictionary:

library = {
    "Python101": "Available",
    "DataScience": "Available",
    "Algorithms": "Available"
}
Menu options:

1 - Add Book
2 - Borrow Book
3 - Return Book
4 - View All Books
5 - Exit
Features:

Add new book (Available)
Borrow → Borrowed
Return → Available
Show all books + statistics
Exit
👉 Extra:

Make book names case-insensitive (lower()).
Track borrowed books in a set.
Prevent adding duplicate books.

"""

library = {
    "Python101": "Available",
    "DataScience": "Available",
    "Algorithms": "Available"
}

##library_lower = {k.lower(): v for k, v in library.items()}
library_lower = {}     
for k, v in library.items():          
    library_lower[k.lower()] = v   

borrowed_books = set()   

def addBook():
    new_book_name = input("Eklenecek kitap adını girin lütfen\n").lower()
    if new_book_name in library_lower:
        print("Bu kitap zaten kayıtlı!")
    else:
        library_lower[new_book_name] = "Available"
def borrowBook():
    borrow_book_name=input("Almak istediğiniz kitabın adını girin\n").lower()

    if borrow_book_name in library_lower:
        if library_lower[borrow_book_name]=="Available":
            library_lower[borrow_book_name]="Borrowed"
            borrowed_books.add(borrow_book_name)
        else:
            print("Kitap başkasına verilmiş")
    else:
        print("istediğiniz kitap elimizde yok")
        
def returnBook():
    return_book_name=input("Ödünç vermek istediğiniz kitabın adını giriniz\n")
    if return_book_name in library_lower:
        if library_lower[return_book_name] == "Available":
            print("Bu kitap zaten kütüphanede.")
        else:
            library_lower[return_book_name] = "Available"
            borrowed_books.discard(return_book_name)
    else:
        print("Böyle bir kitap sistemimizde mevcut değil\n")

def viewAllBook():
    for key, value in library_lower.items():
        print(f"{key}: {value}")

while True:
    print("""
            Menu options:

            1 - Add Book
            2 - Borrow Book
            3 - Return Book
            4 - View All Books
            5 - Exit
        """)
    
    choose = input("Your choose?: ")
    
    if choose == "1":
        addBook()
    elif choose == "2":
        borrowBook()
    elif choose == "3":
        returnBook()
    elif choose == "4":
        viewAllBook()
    elif choose == "5":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")