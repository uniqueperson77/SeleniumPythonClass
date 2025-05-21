def qube(num):
    return num**3


q = lambda num: num**3
print(q(10))

add = lambda x,y: x+y
print(add(6,10))

# print(qube(5))


l=[1,2,3,["a","b","c",[3,6,9]]]
print(l[3][3][2])