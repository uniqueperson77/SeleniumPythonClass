names=["Isha","Sehwag","Dhoni"]
jersey = [1,100,7]
obj = zip(names,jersey)     #tuples
print(list(obj))



l=[10,20,30,40,50]
# l1=[]
# for ele in l:
#     l1.append(ele**2)
# print(l1)

l1 = [ele**2 for ele in l]
print(l1)
