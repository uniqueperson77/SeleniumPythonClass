class Demo:
    def __init__(self,x,y):
        print("This method/constructor gets called automatically as soon as we create an object")
        self.a = x
        self.b = y

    def add(self):
        print(self.a+self.b)

    def sub(self):
        print(self.a-self.b)

    def arith(self):
        self.add()
        self.sub()



d1 = Demo(10,20)  # object/instance
print(d1.a,d1.b)
# print(d1.a)     #obj.var
d1.sub()     #obj.method()
#d2 = Demo()
# print(id(d1))