#types of variable: instance variable and class variable
#instance variable is defined in object __init__
#class variable is defined in class. if this is changed it will change all the object

class car:
    wheel = 5 # class variable

#instance variable
    def __init__(self,brand,rank):
        self.brand = brand
        self.rank = rank

car1=car("audi", 1)
car2=car("Mercedes",2)

print(car.wheel)
print(car1.brand, car1.rank, car2.brand, car2.rank)

