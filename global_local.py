a = 11

def globals_var():
    a = 10

    print(f"inside a value: {a}")

    globals()['a'] = 20



globals_var()
print(a)
