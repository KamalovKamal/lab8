# task 1
# from functools import reduce
# import operator

# def multiply_list(numbers):
#     result = reduce(operator.mul, numbers, 1)
#     return result

# numbers_list = [1,9,10]
# result = multiply_list(numbers_list)
# print (result)

# task 2
# def count_upper_lower(string):
#     upper_count = 0
#     lower_count = 0
    
#     for char in string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
    
#     print(f"Number of Uppercase Letters: {upper_count}")
#     print(f"Number of Lowercase Letters: {lower_count}")

# string = "Hello World! This is a Python Program."
# count_upper_lower(string)

# task 3
# def polindrome(string):
#     string = string.lower()
#     string = string.replace(" ", "")
#     return string == string[::-1]

# word = input(int())
# result = polindrome(word)
# if result:
#     print(word,"yes")
# else:
#     print(word,"not")

# task 4
# import math
# import time
# def square_root(number,):
#     result = math.sqrt(number)
#     return result

# number = int(input())
# after_time = 2123
# time.sleep(after_time/1000)
# result = square_root(number)
# print(result)

# task 5
# list = ('a','abc','ab','cd','df','s','2')
# print(all(list))