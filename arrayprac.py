from array import *

arr = array('i', [])
x = int(input("enter the no. of value: "))

for i in range(x):
    val = int(input("enter the value: "))
    arr.append(val)

print(arr)

z = int(input("which number you want to find: "))
index = 0
for y in arr:
    if z == y:
        print(f"the index value is {index}")
        break
    index += 1


print(arr.index(z))


