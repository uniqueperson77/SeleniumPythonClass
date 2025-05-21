class Parent:
    def parent(self):
        print("This is a parent method")


class Child1(Parent):
    def child1(self):
        print("This is a child1 method")



class Child2(Child1):
    def child2(self):
        print("This is a child2 method")



# p = Parent()
# p.parent()
#
# c1 = Child1()
# c1.parent()
# c1.child1()


c2 = Child2()
c2.parent()

