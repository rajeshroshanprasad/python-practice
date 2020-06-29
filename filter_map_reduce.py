from functools import reduce

lst = []
x = int(input("how many number: "))

for i in range(x):
    a = int(input("enter the number: "))
    lst.append(a)


# filter

fil = list(filter(lambda n : n % 2 == 0, lst))
#map

maap = list(map(lambda n : n * n, fil))

#reduce
reducee = reduce(lambda a,b : a+b, maap)

print(lst)
print(fil)
print(maap)
print(reducee)





