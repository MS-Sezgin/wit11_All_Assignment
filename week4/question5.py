# Soru 5: Bir "Customer" (Müşteri) sınıfı ve bir "Account" (Hesap) sınıfı oluşturun. "Account" sınıfı, 
# bir müşterinin banka hesabı bilgilerini temsil etmek için "Customer" sınıfını kullansın.

# Customer sınıfı özellikleri:

# "name" (müşteri adı)
# "surname" (müşteri soyadı)
# "tc_identification" (müşterinin T.C. kimlik numarası)
# "phone" (müşterinin telefon numarası)

# Account sınıfı özellikleri:

# "customer" (bir Customer nesnesi)
# "account_number" (hesap numarası)
# "balance" (hesap bakiyesi)

# Customer sınıfı metodu:

# display_information(): Müşterinin adını, soyadını, T.C. kimlik numarasını ve telefon numarasını gösterir.

# Account sınıfı metotları:

# deposit(self, amount): Hesaba belirli bir miktar para yatıran metot.
# money_check(self, amount): Hesaptan belirli bir miktar para çeken metot. Ancak hesapta yeterli bakiye yoksa işlem gerçekleşmemeli ve 
# bir mesaj gösterilmelidir.
# display_balance(): Hesap bakiyesini gösteren metot.

# Bu iki sınıfı oluşturun, ardından bir Customer nesnesi ve bir Account nesnesi oluşturun, 
# müşteri bilgilerini Account nesnesine ekleyin, hesap işlemlerini gerçekleştirin ve sonuçları görüntüleyin.

class Customer():
    def __init__(self,name,surname,tc_identification,phone):
        self.name=name
        self.surname=surname
        self.tc_identification=tc_identification
        self.phone=phone
    def display_information(self):
        print(f"name: {self.name} surname: {self.surname} tc_identification: {self.tc_identification} phone:{self.phone}")
class Account():
    def __init__(self,customer,account_number,balance ):
        self.customer=customer
        self.account_number=account_number
        self.balance=balance
    def deposit(self, amount):
        self.balance=self.balance+amount
    def money_check(self, amount):
        if self.balance-amount<0:
            print("Yetersiz bakiye")
        else:
            self.balance=self.balance-amount
    def display_balance(self):
        print(f"Bakiyeniz: {self.balance}")
c=Customer("said","sezgin",222222222222,00000000000)
c.display_information()
a=Account(c,1111111111,9987908798876897)
a.display_balance()
a.money_check(10000)
a.deposit(98789708976)
a.display_balance()