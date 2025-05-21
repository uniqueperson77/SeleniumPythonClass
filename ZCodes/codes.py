def remove_duplicates_from_list(listt):
    # --- Remove the duplicate values from list
    final_list = list(set(listt))       #set removes duplicates and again converting set to list data type
    print(final_list)
    return final_list

# l=[1,2,2,3,4,4]
# final_list = remove_duplicates_from_list(l)
#################################################################

def sum_of_digits(string):
    #--- sum of the digits present in a string
    total = 0
    for char in range(len(string)):
        num = int(char)         #converting every character to int data type
        total = total + num
    print(total)
    return total

# tot = sum_of_digits("13579")
#################################################################

def character_count_in_string(string):
    #--- occurrence of each character from a given string
    dictt = {}
    for char in string:
        if char not in dictt.keys():
            dictt[char] = 1
        else:
            dictt[char] = dictt[char] +1

    print(dictt)
    return dictt

# dictt = character_count_in_string("PythonProgrammingLanguage")
#################################################################
def sorting_list(listt):
    #--- sort an arrary/list in assending or decending order
    asc_list = sorted(listt)
    des_list = sorted(listt,reverse=True)
    print(asc_list,des_list)
    return asc_list,des_list

# asc_list,des_list = sorting_list([2,1,4,7,6,5])

#################################################################
def largest_number_from_an_array(listt):
    # --- largest number from an array
    large = max(listt)
    print(large)
    return large

# largest_number = largest_number_from_an_array([2,1,4,7,6,5])
#################################################################
def second_largest_number_from_an_array(listt):
    # --- Find 2nd Largest Number in an Array
    new_list = remove_duplicates_from_list(listt)   # this removes duplicates first
    asc_list = sorted(new_list)        # arranged in ascending order
    second_large = asc_list[-2]     # this returns 2nd largest
    print(second_large)
    return second_large

# second_largest_number = second_largest_number_from_an_array([2,1,4,7,6,5,7])
#################################################################
def check_palindrome(string):
    #--- entered string or a number is a palindrome or not
    reverse_string = string[::-1]
    if reverse_string == string:
        print("Given string: {} is a palindrome".format(string))
        return True
    else:
        print("Given string: {} is not a palindrome".format(string))
        return False

# status = check_palindrome("madam")
#################################################################
def reverse_words(string):
    # --- reverse the words in a string
    list_of_words = string.split()
    reverse_list_of_words = reversed(list_of_words)
    reverse_words = " ".join(reverse_list_of_words)
    print(reverse_words)
    return reverse_words

# reverse_words = reverse_words("Hi Bro, Where are you")

#################################################################
def reverse_chars_in_each_word(string):
    # --- reverse the characters of each word in a string
    list_of_words = string.split()
    l = []
    for word in list_of_words:
        reverse_word = word[::-1]
        l.append(reverse_word)
    final_string = " ".join(l)
    print(final_string)
    return final_string

# final_string = reverse_chars_in_each_word("Hi Bro, Where are you")

#################################################################
def find_duplicates(listt):
    # find duplicates
    unique_list = list(set(listt))
    duplicate_elements = []
    for value in unique_list:
        if listt.count(value) > 1:
            duplicate_elements.append(value)

    print(duplicate_elements)
    return duplicate_elements

# find_duplicates([1,2,3,2,3,4,5,5,6,7,8])

#################################################################
def find_unique_words(string):
    string = string.lower()
    list_of_words = string.split(" ")
    unique_words = list(set(list_of_words))
    for value in unique_words:
        print(value)
    return True

# find_unique_words("Hi Hello, Good Morning. Hope you are good")
#################################################################
def find_unique_values_in_dict(dictt):
    values = dictt.values()
    unique_values=[]
    for value in values:
        if value not in unique_values:
            unique_values.append(value)

    print(unique_values)
    return unique_values

# find_unique_values_in_dict({1:"Hi",2:"Hello",3:"Hi",4:"Good"})
#################################################################
def swap_without_third_or_temp_variable(a,b):
    b,a= a,b
    print(a,b)
    return a,b
# a,b = swap_without_third_or_temp_variable(5,10)
#################################################################
def unique_chars_in_string(string):
    string = string.lower()
    unique_chars = list(set(string))
    for char in unique_chars:
        print(char, end = " ")
    return True
# unique_chars_in_string("Hi How are You?")
#################################################################
def reverse_num_in_python(num):
    n = str(num)
    reverse_num = int(n[::-1])
    print(reverse_num)
    return reverse_num
# reverse_num_in_python(1234)
#################################################################
def find_large_num(*args):
    large = max(*args)
    print(large)
    return large
# find_large_num(1,5,9,15,14)
#################################################################
def factorial(num):
    val = 1
    for i in range(1,num+1):
        val = val * i
    print(val)
    return val
# factorial(5)
#################################################################
def check_prime(number):
    if number in (1,2):
        print("{} is a prime number".format(number))
        return True

    for i in range(2,number//2+1):
        if number%i==0:
            break
    else:
        print("{} is a prime number".format(number))
        return True
    print("{} is a not prime number".format(number))
    return False

# check_prime(19)
#################################################################
#################################################################
#################################################################