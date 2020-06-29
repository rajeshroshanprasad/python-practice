
a = int(input("Enter the first value:  "))
b = int(input("Enter the second value:  "))

def div(a,b):
    return (a/b)


def smart_div(func):

    def inner(a,b):
        if a < b:
            a,b = b,a

        return func(a,b)

    return inner

div_new = smart_div(div)
result= div_new(a,b)

print(result)





