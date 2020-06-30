#In binary search the values should be shorted
#lower and upper bound, find mid , move  the ;ower and mid depending upon the value to search.

lst = [1,2,33,44,66,88,32,64,785,3245,7884332,6731466,4677,4,236]
lst.sort()
print(lst)
pos = -1
n = 3245

def binary_search(lst,n):
    l = 0
    u = len(lst)-1

    while l <= u:
        mid = (l+u)//2

        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid+1
            else:
                u = mid-1

if binary_search(lst,n):
    print("Found at :" , pos+1)
else:
    print("Not found")





