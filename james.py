
fnum = {2,4,5,7,0}

mnum =  {2,4,6,8,9}

ynum = {1,2,5,6}

print(fnum.intersection(mnum))
print(fnum.union(mnum))
print(fnum.difference(mnum))

print(fnum.difference(ynum.difference(mnum)))
print(fnum.union(mnum.union(ynum)))
print(fnum.intersection(mnum.difference(ynum)))


print(len(fnum))

for item in fnum:
    print(item)

alist = [2,35,1,7,2,2]

blist = alist.sort(reverse=True)

print(alist)


exdict1 = {"name": "James", "Age": 37, "Male": True}

print(exdict1.values())
