# Soru 3: Bir "Shape" (Şekil) sınıfı oluşturun. Bu sınıfın altında "Rectangle" ve "Square" (Kare) adında iki alt sınıf oluşturun.

# "Shape" sınıfının "width" ve "height" olmak üzere iki özelliği olsun.
# "Rectangle" sınıfı "Shape" sınıfından kalıtım alsın ve ek olarak bir calculate_area() metodu içersin.
# "Square" sınıfı da "Shape" sınıfından kalıtım alsın ve karenin alanını aynı calculate_area() metoduyla hesaplasın.

# Bir "Rectangle" ve bir "Square" nesnesi oluşturun, her birinin genişlik ve yüksekliğini belirleyin, her birinin alanını hesaplayın ve sonuçları yazdırın.

class Shape:
    def __init__(self,width,height):
        self.width=width
        self.height=height

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
    def calculate_area(self):
        return self.width*self.height

class Square(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
    def calculate_area(self):
            return self.width*self.height
rec=Rectangle(5,7)
squ=Square(5,7)
print(squ.calculate_area())
print(rec.calculate_area())