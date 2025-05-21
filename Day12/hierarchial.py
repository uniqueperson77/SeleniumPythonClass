class Parent:
    def parent(self,p1=None):
        print("This is a parent method")

    # def parent(self,p1):
    #     print("This is a parent method")


class Child1(Parent):
    def child1(self):
        print("This is a child1 method")
    # def parent(self):
    #     super().parent()
        # print("This is a parent-child1 method")




class Child2(Parent):
    def child2(self):
        print("This is a child2 method")



p = Parent()
p.parent()
p.parent("Hello")
#
# c1 = Child1()
# c1.parent()
# c1.child1()

c1 = Child1()
c1.parent()


# c2 = Child2()
# c2.parent()
# c2.child2()

