list1 = []
list2 = [1,2,3,4,5,"Hello"]
list3 = ["Hi",2.5,True,"World",2]

#access
print(list1)
list1.append("Dhoni")
print(list1)

print(list2.index("Hello"))
print(list2[0],list2[1],list2[5])
for obj in list3:
    print(obj)


l1= [1,2]
l2 = [3,4]
print(l1+l2)
print(l1)
l2.extend(l1)
print(l2)

l=["Hi","World"]
print(l)
l[1] = "Universe"
print(l)





