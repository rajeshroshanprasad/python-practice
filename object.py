class cars:

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color


    def details(self):
        print(f"car brand : {self.brand}  car_color: {self.color}")


car1=cars("BMW", "Red")
car2=cars("AUDI", "Black")

car1.details()
car2.details()
