#1.Write a recursive function named star_string that accepts an integer 
# parameter n and returns a string of stars (asterisks) 2n long (i.e., 2 to the nth power). For example:
# star_string(0) returns "*"" (reason: 2^0 = 1)
# star_string(1) returns "**" (reason: 2^1 = 2)
# star_string(2) returns "****" (reason: 2^2 = 4)

def star_string(n):
    if n < 0:
        raise ValueError
    
    if n == 0:
        return "*"
    else:
        print ('*', end:="" )
        t = 2 * star_string(n-1)
        return t
    

#2. Write a recursive function named digit_sum that accepts an integer as a parameter and returns the sum of its digits. 
# For example, calling digit_sum(1729) should return 1 + 7 + 2 + 9, which is 19.If the number is negative, return the negation
# of the value. For example, calling digit_sum(-1729) should return -19.
#Constraints: Do not declare any global variables. Do not use any loops you must use recursion. 
# Do not use any auxiliary data structures like list, dict, set, etc. Also do not solve this problem using a string. You can declare 
# as many primitive variables like ints as you like. You are allowed to define other "helper" functions 
# if you like they are subject to these same constraints.

def digit_sum(n):
    i = 1
    if n < 0:
        i = -1
        n = abs(n)
    
    remainder = n % 10
    quotient = n//10
    
    if(quotient == 0):
        return remainder * i
    else:
        return (digit_sum(quotient) + remainder) * i


#3. Write a recursive function named stutter_list that accepts a list of integers as a parameter and 
# replaces every value in the list with two occurrences of that value. 
# For example, suppose a list named s stores these values, from bottom => top:
# [13, 27, 1, -4, 0, 9]
# Then the call of stutter_list(s) should change the list to store the following values:
# [13, 13, 27, 27, 1, 1, -4, -4, 0, 0, 9, 9]
#Notice that you must preserve the original order. In the original list the 9 was at the top and would 
# have been popped first. In the new list the two 9s would be the first values popped from the list. 
# If the original list is empty, the result should be empty as well.
#Constraints: Your solution must be recursive. Do not use any loops. Do not use any auxiliary collections or 
# data structures to solve this problem.
def stutter_list(my_list): 
    if len(my_list) == 0:
        pass
    else:
        value = my_list.pop()
        stutter_list(my_list)
        my_list.append(value)
        my_list.append(value)
        

#4. Write a recursive function named reverse that accepts a string parameter and returns that string with its characters in the opposite order. 
# For example, the call of reverse("Hi you!") should return "!uoy i_h" .
# Constraints: Do not use any loops you must use recursion. Do not declare any global variables or any auxiliary data structures.
def reverse(num):
    if len(num) == 0:
        return ""
    else: 
        return num[-1] + reverse(num[:-1])