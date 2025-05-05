#Task1:
#1 to 50 numbers -> print only even numbers

# for num in range(1,51):
#     if num%2==0:
#         print(num)


#Task2:
#1 to 50 numbers -> print only odd numbers

# for num in range(1,51):
#     if num%2!=0:
#         print(num)


#Task3
#1 to 50 numbers, I want you to print all numbers except numbers which were multipes of 12

# for num in range(1,51):
#     # if num%12==0:
#     #     continue
#     # print(num)
#
#     if num%12==0:
#         pass
#     else:
#         print(num)

#PS: add the numbers from 1 to 10 and print the result  #n(n+1)/2
# val = 10
# sum = 0
# for num in range(1,val+1):
#     sum = sum + num
#     # sum+=num
# print(sum)
#
# sum2 = val*(val+1)/2        #returns float value
# sum3 = val*(val+1)//2        #returns int value
# print(sum2,sum3)

def add(value):
    result = 0      #sum
    start =1       #iterable => increased by 1 everytime
    while start<=value:       #start <value+1, start <=value
        result = result+start
        start = start+1
    print(result)

# add(10)

#Hello World  => 'o' don't print only 'o'
var = "Hello World"
# print(var[1])

for char in var:
    if char != 'o':
        print(char)






