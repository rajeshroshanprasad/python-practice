lst = []

y = int(input(" the number you want to append: "))

i = 0
while i < y:
    x = int(input(" the number: "))
    lst.append(x)
    i += 1


def count(lst):
    even = 0
    odd = 0
    for i in lst:
       if i % 2 == 0:
           even += 1


       else:
           odd += 1

    return even,odd


even,odd = count(lst)
print(f"No of even number: {even}, No of odd number: {odd}")




