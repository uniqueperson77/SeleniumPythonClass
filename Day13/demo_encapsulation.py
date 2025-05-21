class Employee:
    def __init__(self,name,salary,position):
        self.name = name
        self.__salary = salary
        self.position = position

    def __get_salary(self):
        print(self.__salary)

    def set_salary(self,new_salary):
        self.__salary = new_salary
        self.__get_salary()


obj = Employee("Isha","50K $","SDE")
print(obj.name)
# obj.get_salary()
obj.set_salary("100K $")
obj.__get_salary()