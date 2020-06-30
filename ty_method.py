#types of method

#Accessors: they fetch the value from instance variable and mutators: they change the value.

class student:

    def __init__(self,name,marks1,marks2):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2

    def avg(self):
        return (self.marks1 + self.marks2)



s1 = student('rajesh', 39, 59)
s2 = student('dhiraj', 80, 85)

print(s1.avg())
print(s2.avg())








