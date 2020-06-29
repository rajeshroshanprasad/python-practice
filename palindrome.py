#given string is palindrome or not

x = int(input(" enter to check for palindrome: "))

print(str(x)[::-1])

if str(x) == str(x)[::-1]:
    print("Plaindrome")

else:
    print("not a palindrome")



