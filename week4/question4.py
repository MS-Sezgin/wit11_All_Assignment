# Soru 4: Python'da bir "Vehicle" (Araç) sınıfı oluşturun. Bu sınıfın aşağıdaki özelliklere sahip olduğundan emin olun:

# Özellikler:

# "make" (aracın markası)
# "model" (araç modeli)
# "year" (aracın üretim yılı)

# "Vehicle" sınıfını oluşturun ve ondan türetilen "OffRoadVehicle" (SUV) ve "SportsCar" (Spor Araba) adında iki alt sınıf oluşturun.

# "OffRoadVehicle" sınıfı "Vehicle" sınıfından kalıtım alsın ve ek olarak "four_wheel_drive" (dört çeker) özelliğini eklesin.
# "SportsCar" sınıfı "Vehicle" sınıfından kalıtım alsın ve ek olarak "max_speed" (maksimum hız) özelliğini eklesin.

# Her sınıftan birer nesne oluşturun, özelliklerini belirleyin ve bu özellikleri ekranda gösteren bir program yazın.

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def show(self):
        print(f"{self.year} {self.make} {self.model}")

class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year,four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive=four_wheel_drive
    def show(self):
        super().show()
        print(f"4x4: {self.four_wheel_drive}")
class SportsCar(Vehicle):
    def __init__(self, make, model, year,max_speed):
        super().__init__(make, model, year)
        self.max_speed=max_speed
    def show(self):
        super().show()
        print(f"max speed: {self.max_speed}")

v=Vehicle("bmw","s",2021)
o=OffRoadVehicle("bmw","s",2021,4)
s=SportsCar("bmw","s",2021,350)
v.show()
o.show()
s.show()
