n = input("enter the value: ")
isUnique = True
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] == n[j]:
            isUnique = False
            break

if isUnique:
    print("unique")

else:
    print("not unique")




