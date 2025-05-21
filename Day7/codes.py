num1 = int(input("Enter the number larger than 1 -> "))
num2 = int(input("Enter the number larger than 1 -> "))


def IsPrime(num):
    c = 0
    for x in range(2, num + 1):
        if num % x == 0:
            c += 1
    # print("count value:", c)
    if c == 1:
        print("Given number {} is prime".format(num))
        return True
    else:
        print("Given number {} is not prime".format(num))
        return False


for number in range(num1,num2+1):
    IsPrime(number)


## Task1: don't use in-built sort, using for or while, try to sort the given list which contains only numerics
## Task2: implement user defined reverse using loop structers
## Task3: try to implement palindrome logic, fibonacci series