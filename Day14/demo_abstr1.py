#in abstract classes - we will declare the methods (declaration)
#child classes - u need to implement the abstarct methods

# from abc import ABC
# from abc import abstractmethod

from abc import *
# import abc

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class Tiger(Animal):
    def eat(self):
        print("Tiger is having something")


Tiger().eat()
# ob = Tiger()
# ob.eat()
