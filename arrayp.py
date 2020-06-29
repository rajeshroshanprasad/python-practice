from array import *
vals = array('i',[2,4,3,5,6])


newarrr= array(vals.typecode, (a*a for a in vals))

for j in newarrr:
    print(j)


print()


for i in range(len(vals)):
    print(vals[i])








