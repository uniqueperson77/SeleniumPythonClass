def func2():
    pass

# func2()     #calling

def func3(parameter):
    print(parameter)

# func3(5.5)

def addition(p1,p2,p3):
    global val      #can be written inside functions only
    val = p1+p2+p3      #val is local variable
    print(val)
    return val



# sum=addition(3,5,7)     #calling
# l = (3,10)
def mutliplication(*args):      # handling dynamic parameters
    result = 1
    for val in args:
        result = result*val
    return result

# result = mutliplication(3)
# print(result)

def mutliplication1(*args):      # handling dynamic parameters
    result = 1
    for val in args:
        result = result*val
    return result

# result = mutliplication1(10,20,30,40)
# print(result)

def func5(**kwargs):
    print(kwargs)
    print(type(kwargs))


func5(x=10,y=20)
# func5(10,20)



