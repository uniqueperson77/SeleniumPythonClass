numbers=[1,2,3,4,5,6,7,8,9,10]
# odd numbers list

# ol=[]
# for item in l:
#     if item%2!=0:
#         ol.append(item)
#
# print(ol)


ol =list(filter(lambda y: y%2!=0,numbers))
print(ol)

el =list(filter(lambda y: y%2==0,numbers))
print(el)
