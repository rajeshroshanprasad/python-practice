#class and object

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = person("raj", 30)
c2 = person("aak", 30)

if c1.compare(c2):
    print("Same person")

else:
    print("different person")

print(c1.name, c1.age)
print(c2.name, c2.age)

