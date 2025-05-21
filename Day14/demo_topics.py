#map

l=[1,2,3,4,5]
l1=["1","2","3","4"]
print(float(l1[0]))
# l= [1,2,9,16,25]

obj = map(float,l1)
print(list(obj))
# exit()
s="abcde"
print(s.upper())
exit()


def func(item):
    return item*2

def func1(item):
    return item.upper()

print(list(map(func1,s)))
exit()

l1 = list(map(func,l))
print(l1)

# l1 =[]
# for val in l:
#     f_value = func(val)
#     l1.append(f_value)
#
# print(l1)
