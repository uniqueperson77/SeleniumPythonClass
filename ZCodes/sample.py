import sys
l=[1,2,3,4,5]
t = tuple(l)
print(sys.getsizeof(l),sys.getsizeof(t))
def func(i):
    return i**2

print(list(map(float,l)))
print(list(map(func,l)))

def func1(i):
    if i%2 ==0:
        return i**2
print(list(filter(func1,l)))

#
l3 = [1,2,3,4,5]
l4 = ["A","B","C","D","E"]
z = zip(l3,l4)
l5 = list(z)
print(l5)       #zip object to list object  ##[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]
print(sys.getsizeof(l3),sys.getsizeof(l4),sys.getsizeof(z),sys.getsizeof(l5))

#
l2 = [i+10 for i in l]
print(l2)

def count_upto_max(num):
    count =1
    while count<=num:
        yield count
        count = count +1


for number in count_upto_max(5):
    print(number)

def my_decorator(fun):
    def f1():
        print("I will pack this using tape, papers")
        fun()
        print("Packing finished.")
    return f1

@my_decorator
def box():
    print("This is box.")

box()