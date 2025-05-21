from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass        #declaration


class Bike(Vehicle):
    def start(self):    #implementation
        print("Bike got started")



# obj = Vehicle()       #object can't be created for the class which is having abstract method
obj = Bike()
obj.start()