#Define a lambda expression named f that accepts two string parameters representing a first 
# and last name and concatenates them together to return a string in "Last, First" format. 
# For example, if passed "Cynthia" and "Lee", it would return "Lee, Cynthia". Do not write an 
# entire function; just write a statement of the form:
#f = lambda parameters: expression

f = lambda x,y :  y + ', ' + x

#Define a lambda expression named f that accepts two integer parameters and returns the larger of 
# the two; for example, if passed 4 and 11, it would return 11. Do not write an entire function; just 
# write a statement of the form:
f = lambda x,y : y if y > x else x

#Define a lambda expression named f that accepts an integer parameter and converts it into the 
# square of that integer; for example, if 4 were passed, your lambda would return 16.
# Do not write an entire function; just write a statement of the form:
f = lambda x: x * x


#Write a function named abs_sum that takes a list of integers as a parameter and returns the sum 
# of the absolute values of each element in the list. For example, the absolute sum of [-1, 2, -4, 6, -9] is 22. 
# If the list is empty, return 0.Use Python's functional programming constructs, such as list comprehensions, map,
# filter, reduce, to implement your function. Do not use any loops or recursion in your solution.

import functools 
def abs_sum(int_num):
    if len(int_num) > 0:
        abs_list = map(lambda n: abs(n), int_num)
        f = functools.reduce(lambda x,y : x + y, abs_list)
        return f
    else:
        return 0 
        
#Write a function named count_negatives that takes a list of integers as a parameter and returns how many numbers 
# in the list are negative. For example, if the list is [5, -1, -3, 20, 47, -10, -8, -4, 0, -6, -6], you should 
# return 7. Use Python's functional programming constructs, such as list comprehensions, map, filter, reduce, to 
# implement your function. Do not use any loops or recursion in your solution.
def count_negatives(list_int):
    minus = lambda values: values < 0
    length = list(filter(minus, list_int))
    return len(length)

#Write a function named double_list that takes a list as a parameter and returns a list of integers that contains 
# double the elements in the initial list. For example, if the initial list is [2, -1, 4, 16], you should return 
# [4, -2, 8, 32].Use Python's functional programming constructs, such as list comprehensions, map, filter, reduce, to 
# implement your function. Do not use any loops or recursion in your solution.
def double_list(list_param):
    double_elemtnts = list(map(lambda x: x*2, list_param))
    return double_elemtnts

#Write a function called four_letter_words accepts a string representing a file name as a parameter and returns a 
# count of the number of words in the file that are exactly four letters long. Words are separated by whitespace. 
# Do not worry about punctuation; look for any four-character token.Use Python's functional programming constructs, 
# such as list comprehensions, map, filter, reduce, to implement your function. Do not use any loops or recursion in 
# your solution.
def four_letter_words(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        four_letter_words_count = len(list(filter(lambda x: len(x) == 4, words)))
        return four_letter_words_count
    
#Write a function called glue_reverse that accepts a list of strings as its parameter and returns a single string 
# consisting of the list's elements concatenated together in reverse order. For example, if the list 
# stores ["the", "quick", "brown", "fox"], you should return "foxbrownquickthe".If the list is empty, return an empty string, "".
import functools
def glue_reverse(list_string):
    if len(list_string) > 0:
        f = lambda x,y: y+x
        n = functools.reduce(f, list_string)
        return n
    else:
        return ""
    

#Write a function named largest_even that takes a list of integers as a parameter and returns the largest even number 
# from a list of integers. An even integer is one that is divisible by 2. For example, if the list is [5, -1, 12, 10, 2, 8],
# your function should return 12. You may assume that the list contains at least one even integer.
def largest_even(list_int):
    if len(list_int) > 1:
        f = list(filter(lambda x : x % 2 == 0, list_int))
        n = functools.reduce(lambda x,y: x if x > y else y, f)
        return n
    else:
        return list_int[0]

#Suppose you have a list of strings declared as follows. Write functional code to produce a new list named words2 
# containing all of the three- or four-letter words in the list. words = ["four", "score", "and", "seven", "years", "ago"]
n = (lambda x : len(x) == 3 or len(x) == 4 )
words2 = list(filter(n, words))

#Write a function named total_circle_area that accepts a list of real numbers representing the radii of the circles as 
# a parameter and returns the sum of the areas of a group of circles, rounded to the nearest integer. Recall that the 
# area of a circle of radius r is π r2. For example, if the list is [3.0, 1.0, 7.2, 5.5], your function should return 
# 289. If the list is empty, return 0.
import math
def total_circle_area(list_num):
    if len(list_num) > 0:
        area = list(map(lambda x: math.pi * x * x, list_num)) #[28.26, 3.14, 162.776]
        f = lambda x,y: x+y
        total_area = round(functools.reduce(f, area))
        return total_area
    else:
        return 0