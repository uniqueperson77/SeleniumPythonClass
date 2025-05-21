list1 = ["Hi","Hello","World"]
list2 = [1,2,3,4,5,"Hello",1,2,3]
list3 = ["Hi",2.5,True,"World",2]
list4 = [3,5,7,4,2,1,9]

list4.sort()        #ascending
print(list4[0])     #min
print(list4[len(list4)-1])     #max

print(min(list4))
print(max(list4))

exit()



#slicing (sub-list)
list4[2] = "New Value"
print(list4)
exit()
print(list4[1:6])
print(list4[1:])
print(list4[:4])
print(list4[4])     # straight
print(list4[-3])    #reverse
exit()

print(list4)
list4.reverse()
print(list4)
exit()

# lists methods
#ascending order
# print(list4)
# list4.sort()
# print(list4)

#descending order
print(list4)
list4.sort(reverse=True)        #descending
print(list4)
exit()
###########################
list1.pop(1)
print(list1)

exit()
print(len(list1))       #length
print(list1)
for val in list1:
    if val == "Hi":
        list1.remove(val)
print(list1)



exit()
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



