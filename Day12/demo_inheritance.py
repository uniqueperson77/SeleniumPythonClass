class Parent:
    a="Hi"

    def method1(self):
        print("I am parent method.")

class Parent2:
    b="Hello"
    def method3(self):
        print("I am parent2 method.")

class Child(Parent):            #simple Inheritance
    def method2(self):
        print("I am child method.")


class Child1(Parent,Parent2):
    pass



c_obj = Child1()
c_obj.method1()
c_obj.method3()


exit()
c_obj = Child()
print(c_obj.a)
c_obj.method1()
c_obj.method2()

p_obj = Parent()
p_obj.method1()