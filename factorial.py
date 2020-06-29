#factorial of a number

n = int(input("enter the number: "))


def facto(n):
    a = 1
    for i in range(2, n+1):
        a = a*i

    print(a)




facto(n)