#Write a function named circle_area that accepts the radius of a circle as a parameter (as a number)
# and returns the area of a circle with that radius. For example, the call of area(2.0) should 
#return 12.566370614359172. You may assume that the radius passed is a non-negative number.
def circle_area(radius):
    pi = 3.14159
    return pi * radius ** 2

# <--------------------------------------------------------------------------------------------------------------------------------------------->

'''Given the following variable declarations, what is the value of each of the following Boolean
expressions? Write True or False for each.
x= 27
y = -1
z = 32
b = False

not b	-------> True 
b or True  -------> True 
(x > y) and (y > z)	-------> False 
(x == y) or (x <= z) ------->	True 
not (x % 2 == 0)	-------> True 
(x % 2 != 0) and b	------->False 
b and not b	------->False 
b or not b	------->True 
(x < y) == b	------->True 
not (x / 2 == 13) or b or (z * 3 == 96)	------->True 
(z < x) == False	------->True 
not ((x > 0) and (y < 0))	------->False
'''

'''
Write a function named average_of_2 that takes two integers as parameters and returns the average 
of the two integers. For example, the call of average_of_2(2, 9) should return 5.5.
'''
def average_of_2(a, b):
    return (a+b)/2 

# <--------------------------------------------------------------------------------------------------------------------------------------------->

'''
The following function attempts to return the median (middle) of three integer values, but it 
contains logic errors. In what cases does the function return an incorrect result? How can the code
be fixed? Determine what is wrong with the code, and submit a corrected version that works properly.
'''
def median_of_3(n1, n2, n3):
    if n1 < n2:
        if n2 < n3:
            return n2
        elif n1 < n3:
            return n3
        else:
            return n1
    else:
        if n1 < n3:
            return n1
        elif n2 < n3:
            return n3
        else:
            return n2
        
# <--------------------------------------------------------------------------------------------------------------------------------------------->

'''
Write a function named count_digits that accepts an integer parameter and returns the number of 
digits in that integer. For example, count_digits(38015) returns 5. For negative numbers, return 
the same value as if the number were positive. For example, count_digits(-72) returns 2.
'''
import math
def count_digits(a):
    abs_ = math.abs(a)
    in_string = str(abs_)
    return len(in_string)

# <--------------------------------------------------------------------------------------------------------------------------------------------->

'''
Write a function named box_of_stars that accepts two integer parameters representing a width and 
height in characters, and prints to the console a 'box' figure whose border is * stars and whose 
center is made of spaces. For example, the call of box_of_stars(8, 5) should print the following 
output:

********
*      *
*      *
*      *
********
You may assume that the values passed for the width and height are at least 2.
'''
def box_of_stars(width, height):
    print('*' * width)
    
    for i in range(height-2):
        print('*' + ' ' * (width -2)+ '*')
        
    print ('*' * width)
    
# <--------------------------------------------------------------------------------------------------------------------------------------------->
    
'''
Write a function named coin_flip that simulates repeatedly flipping a two-sided coin until a 
particular side (Heads or Tails) comes up several times consecutively (in a row). Your function
accepts two parameters, an integer k and a character side, where side is expected to be 'H' for 
Heads or 'T' for Tails. You should keep simulating the flipping of the coin until k occurrences 
of the given side are seen consecutively. For example, if the call is coin_flip(3, 'H') , you 
should flip the coin until Heads is seen 3 times in a row. Here is an example output from the call of
coin_flip(4, 'T')
T H T H T T H T T H H T H H H H H T T T T
You got T 4 times in a row!

If a negative k is passed, and/or a side value is passed that is not 'H' or 'T', your function should prERROR! and exit 
immediately.

Use random or randint to give an equal chance to a head or a tail appearing. Each time the coin is flipped, what is seen 
is displayed (H for heads, T for tails), separated by spaces. When k consecutive occurrences of the given side occur, a 
congratulatory message is printed. Match our output format exactly.
'''
import random
def coin_flip (k, side):
    if k < 0 or side not in ['H', 'T']:
        print("ERROR!")
        return

    
    flips = []
    consecutive_count = 0

    while True:
        if k == 0:
            print(f"\nYou got {side} {k} times in a row!")
            break
        flip_result = 'H' if random.randint(0, 1) == 0 else 'T'
        flips.append(flip_result)
        print(flip_result, end=' ')

        if flip_result == side:
            consecutive_count += 1
        else:
            consecutive_count = 0

        if consecutive_count == k:
            print(f"\nYou got {side} {k} times in a row!")
            break

# <--------------------------------------------------------------------------------------------------------------------------------------------->
        
'''
Write a function named average_length of code that computes and returns the average string length of the elements 
of a list of strings. For example, if the list contains ["belt", "hat", "jelly", "bubble gum"], the average length 
returned should be 5.5. Assume that the list has at least one element.
'''
def average_length(a_list):
    total_letters = 0
    total_length = len(a_list)
    for x in a_list:
        total_letters = total_letters + len(x)
    
    return total_letters/total_length

# <--------------------------------------------------------------------------------------------------------------------------------------------->

'''
Write a function is_palindrome that accepts a list of strings as its argument and returns True if that list is a 
palindrome (if it reads the same forwards as backwards) and False if not. For example, the list 
["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"] is a palindrome, so passing that list to your function
would return True. Lists with zero or one element are considered to be palindromes.
'''
def is_palindrome (a_list):
    reverse_list = a_list[::-1]
    if len(a_list) <= 1:
        return True
    if (a_list == reverse_list):
        return True
    else:
        return False

# <--------------------------------------------------------------------------------------------------------------------------------------------->

'''
Write a function max_length that accepts as a parameter a set of strings, and that returns the length of the longest 
string in the set. If your function is passed an empty set, it should return 0.
'''
def max_length(length_of_set):
    if len(length_of_set) == 0:
        return 0
    else:
        long_length = 0
        lil = list(length_of_set);
        for x in range(0, len(lil)):
            length_of_list = len(lil[x])
            if(length_of_list > long_length):
                long_length = length_of_list
    return long_length
               
 # <---------------------------------------------------------------------------------------------------------------------------------------------> 
            
'''
Write a function named collapse that accepts a list of integers as a parameter and returns a new list where each pair of
integers from the original list has been replaced by the sum of that pair. For example, if a list called a 
stores [7, 2, 8, 9, 4, 13, 7, 1, 9, 10], then the call of collapse(a) should return a new list
containing [9, 17, 17, 8, 19]. The first pair from the original list is collapsed into 9 (7 + 2), the second pair is 
collapsed into 17 (8 + 9), and so on.
If the list stores an odd number of elements, the element is not collapsed. For example, if the list had
been [1, 2, 3, 4, 5], then the call would return [3, 7, 5]. Your function should not change the list that is passed as
a parameter.
'''
def collapse(num_list):
    new_list = list(num_list) 
    print (new_list)
    an_list = []
    if(len(num_list)%2 == 0):
        for x in range(0, len(num_list)-1, 2):
            an_list.append(new_list[x] + new_list[x+1])
        return an_list
    else:
        new_list.append(0)
        print(new_list)
        for x in range(0, len(new_list)-1, 2):
            an_list.append(new_list[x] + new_list[x+1])      
        return an_list
    
# <--------------------------------------------------------------------------------------------------------------------------------------------->    

'''
Write a function named is_stack_sorted accepts a list of integers as a parameter and treats it as a stack, returning 
True if the elements in the stack occur in ascending (non-decreasing) order from bottom (end) to top (front), else False.
This essentially means that you are checking whether the list is in reverse-sorted order. An empty or one-element stack 
is considered to be sorted. For example, if passed the following stack, your function should return True:
[20, 20, 17, 11, 8, 8, 3, 2]
The following stack is not sorted (the 15 is out of place), so passing it to your function should return a result of False
[18, 12, 15, 6, 1]
You should treat the list as a stack and not use any index-related operations on it. This means that the only operations you should use on the
list are the pop and append functions and the len function. You should not use the [] indexing operator nor any other operations that depend on 
accessing various elements by index. You also should not use a for-each loop over the stack's elements.

When your function returns, the stack should be in the same state as when it was passed in. In other words, if your function modifies the stack, 
you must restore it before returning.

Constraints: You may use one list as auxiliary storage. Do not declare any other auxiliary data structures, but you can have as many simple variables 
as you like. Your solution should run in O(N) time, where N is the number of elements of the list.
'''
def is_stack_sorted(stack):
    # Check if the stack is empty or has only one element
    if len(stack) <= 1:
        return True

    # Auxiliary stack to store elements temporarily
    temp_stack = []

    # Variable to keep track of whether the stack is sorted
    sorted_stack = True

    # Pop elements from the original stack and push them to the temp_stack
    while len(stack) > 0:
        current_element = stack.pop()

        # Check if the current element is greater than the top of the temp_stack
        if len(temp_stack) > 0 and current_element < temp_stack[-1]:
            sorted_stack = False
        

        # Push the current element to the temp_stack
        temp_stack.append(current_element)

    # Pop elements from the temp_stack and push them back to the original stack
    while len(temp_stack) > 0:
        stack.append(temp_stack.pop())

    return sorted_stack
# <--------------------------------------------------------------------------------------------------------------------------------------------->

'''
Write a function named has_duplicate_value that accepts a dictionary from strings to strings as a parameter and returns True if any two keys map
to the same value. For example, if a dictionary named m stores {'Marty': 'Stepp', 'Stuart': 'Reges', 'Jessica': 'Miller', 'Amanda': 'Camp',
'Meghan': 'Miller', 'Hal': 'Perkins'}, the call of has_duplicate_value(m) would return True because both 'Jessica' and 'Meghan' map to the 
value 'Miller'. Return False if passed an empty or one-element dictionary. Do not modify the dictionary passed in.
'''
def has_duplicate_value (m):
    my_string = set()
    if len(m) <= 1:
        return False
    for value in m.values():
        if value in my_string:
            return True
        my_string.add(value)
    return False
        
# <--------------------------------------------------------------------------------------------------------------------------------------------->       

'''
Write a function named remove_duplicates that accepts as a parameter a list of integers, and modifies it by removing any duplicates.
Note that the elements of the list are not in any particular order, so the duplicates might not occur consecutively. You should retain the original
relative order of the elements. Use a set as auxiliary storage to help you solve this problem. For example, if a list named v 
stores [4, 0, 2, 9, 4, 7, 2, 0, 0, 9, 6, 6], the call of remove_duplicates(v) should modify it to store [4, 0, 2, 9, 7, 6].
'''
def remove_duplicates(list_of_integers):
    unique_nums = set()
    index = 0
    while index < len(list_of_integers):
        num = list_of_integers[index]
        if num not in unique_nums:
            unique_nums.add(num)
            index += 1
        else:
            list_of_integers.pop(index)
# <--------------------------------------------------------------------------------------------------------------------------------------------->