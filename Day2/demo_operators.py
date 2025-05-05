import math

def arithemetic():
    x=100
    y=22

    print(x+y)
    print(x-y)

    print(x*y)
    print(x/y)
    print(x//y)

    print(x%y)  #remainder

    print(10**2) #exponential

    print(int(math.sqrt(100)))

# arithemetic()

def Comparison():
    x= 20
    y=30
    # comparsion boolean values => True False

    # result = x==y
    # print(result)

    print(x==y)
    print(x!=y)
    print(x>y)
    print(x<y)
    print(x>=y)
    print(x<=y)


def logical():
    x= True
    y= False
    z= True
    print(x and y and z)      #=> all values should be True then it will return True
    print(x or y)       #=> atleast one value should be high to return high
    print(not x)

# logical()

def Assignment():
    a = 10
    b= 20
    print(a)
    # a=a+b
    # a+=b
    # a-=b
    a*=b
    print(a)

# Assignment()

def Membership():
    name = "Isha"
    # if "b" in name:
    #     print("character s is present")
    # else:
    #     print("not present")

    if "b" not in name:
        print("character b is not present")
    else:
        print("present")

# Membership()

# a = 100
# c = 100
# b = 1000
# print(id(a), id(b),id(c))
# a = b
# print(id(a), id(b))

def Identity():
    a=100
    b=100
    print(a is not b)

Identity()

