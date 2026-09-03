"""

✅ Project 4: Mini Market Basket
Practice dictionaries and loops.

Products and prices:

products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}
Ask the user for 3 products.

Calculate total price.

Print:

Your basket: apple, banana, milk
Total price: 12 TL
If a product doesn’t exist → print warning.

"""

products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}

requestList = input("\nAlmak istediğiniz 3 ürünün adını aralarında boşul bırakarak giriniz\n").split()
basketValue=0
basketList=[]

for i in requestList:
    if i in products:
        basketValue += products[i]
        basketList.append(i)
    else:
        print(f"{i} ürünü elimizde yok")

print(f"""Your basket: {basketList}
        Total price: {basketValue} TL""")