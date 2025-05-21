# Task, we have been given a string => we need to print the string by removing vowels
name = "HEllo"

vowel_list= ['a','e','i','o','u']
# print(name)
name = name.lower()
# print(name)
final_name = ""
for char in name:
    if char in vowel_list:
        pass
    else:
        final_name = final_name + char
        # print(char,end="\n")
    print(final_name)

print("**After completion of loop **")
print(final_name)


#Task1: 19 -> check whether this num is prime or not
#Task2: 1,25 -> print all the prime numbers in the given range

#Task3: 1,25 -> print all the prime numbers in the given range but utilize functions concept

# def check_prime(num):
#     #st1
#     #logic
#     pass



