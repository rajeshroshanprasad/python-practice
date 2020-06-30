lst = [2,4,5,7,6,1,10,9]
i = 0
n = 5
pos = -1
isunique = False
while i < len(lst):
    if lst[i] == n:
        isunique = True
        globals()['pos']= i
    i = i + 1


if isunique:
    print("Found at : ", pos+1)
else:
    print("not found")





