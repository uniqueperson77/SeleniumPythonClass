#1 to 10 numbers
# print(1)
# print(2)
# print(10)

# import ctypes
# x=100
# memory_address = id(x)
# print("memory_address: " + str(memory_address))
#
# obj = ctypes.cast(memory_address,ctypes.py_object)
# value_of_x = obj.value
# print("value: "+ str(value_of_x))


#0,1,2, 10
#ps: whenever value reached 3 - exit from loop (break)
# for value in range(1,101):        #1,2,3,4,5
#     print(value)
#     if value == 3:
#         break


#continue -> skip the current iteration & move to further iterations
names = ["Sachin","Dhoni","Sehwag","Virat","Zaheer"]
#access
# print(names[2])

#skip Sehwag to bat
target_var = "Sehwag"
# for index in range(len(names)):     ## target to access using index
#     if names[index] == target_var or names[index] == "Zaheer":
#         continue
#     print(names[index] + " is a new batter.")

for val in names:
    if  val == "Zaheer":
        continue
    print(val + " is a new batter.")










