set1 = {1,2,3,4,5,3,4,6}
print(set1)
set2 = {2,4,7,6}

set7 = set()        #declare an empty set
print(type(set7))

## access
#set1.pop()
set5 = set1.intersection(set2)
set6 = set5
print(set1.union(set2))
print(id(set5),id(set6))
# print(set5,set6)
# set5.add(8)
# print(set5,set6)

set7 = set5.copy()
print(id(set7))
set5.add(9)
print(set5,set7)
exit()

set1.remove(5)
print(set1)
set1.add(5)
print(set1)
set1.clear()
print(set1)

exit()
set3 = {1,3,5,"Hello","Hi","Hi"}
print(set3)

set2 = set("Hello")
print(set2)

l = [2,4,4]
l2 = list(set(l))
print(l2)