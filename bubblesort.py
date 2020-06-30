lst = [2,1,3,15,10,14,12,9,8,18,26]
def sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                c = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = c


sort(lst)
print(lst)