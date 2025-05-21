dict1 = {}
dict2 = dict()
print(dict1,dict2)
dict3 = {1:"Rahul",2:"Rahul","Id1":"Sachin","Id2":"Sehwag"}
print(dict3)

dict5 = dict3.copy()
dict5.setdefault(3,"Zaheer")
print(dict5,dict3)
print(len(dict5))


exit()

for key,value in dict3.items():
    print(key,dict3.get(key))

l= [3,6,9]
for index,val in enumerate(l):
    print(index,val)

exit()

for key in dict3.keys():
    # print(dict3[key])
    print(dict3.get(key))

for value in dict3.values():
    # print(dict3[key])
    print(value)





exit()
print(dict3)
dict3[4] = "Dhoni"
print(dict3)
dict3.setdefault(5,"Sachin")
print(dict3)

dict3.pop(4)
print(dict3)

dict4 = dict3.copy()
keys = dict4.keys()
values = dict4.values()
print(keys,values)
print(dict4.items())



# print(dict3,dict4)
# dict4.clear()
# print(dict3,dict4)