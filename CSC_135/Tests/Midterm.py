import functools 
from List135 import rest

        

def maxevens(xs):
    nm = list(filter(lambda x : x%2 == 0, xs))
    val = functools.reduce(lambda x,y : x if x>y else y, nm)
    return val
maxevens([1,2,3,4,5,6])
# Write a function max_nonempty that takes a nonempty python list
# of numbers and returns the largest number. Use reduce to do this by
# using the builtin function max(a,b) in your lambda.
def max_nonempty(xs):
    val = functools.reduce(lambda x,y: max(x,y), xs)
    return val
max_nonempty([-1, 2, 0])
# Write a function that uses some combination of map, reduce, filter
# and/or lambda that takes a python list of numbers xs and a number c as
# parameters and produces a python list of the distances each element
# x is from c (ie, abs(x-c)). For example dists([-1, 2, 0], 1) should return
# [2, 1, 1]. You may use the builtin function abs(x) in your lambda.
def dists(xs, c):
    val = list(map(lambda x: abs(x-c),xs))
    return val

dists([-1, 2, 0], 1) #returned [2, 1, 1]

# Problem 3: Write a recursive function firstN that takes a List135 xs as a
# parameter and returns a new List135 composed of the first n elements
# of xs. For example firstN([1,2,3], 2) would produce [1,2]. You may
# assume 0 <= n <= len(xs). Hint: n == 0 is your base case.
from List135 import List135 
def firstN(xs, n):
    if n == 0:
        pass
    else:
        newNode = List135()
        val = newNode.add(xs[0])
    return firstN(xs[1:], n-1)

firstN([1,2,3], 2)

# Problem 4: The following function returns how many elements of a List135
# are greater than x. Rewrite it to be tail recursive. You may add a helper
# function or an extra parameter with a default value if you want to.
'''
def num_greater(xs, x):
    if xs.empty():
        return 0
   else:
        cnt = 0
        if xs.first() > x:
           cnt = 1
        return cnt + num_greater(xs.rest(), x)
'''
def num_greater(xs,x):
    return _num_greater(xs,x,0)

def _num_greater(xs,x,acc):
    if xs.empty():
        return acc
    else:
        if acc > x:
            return (xs[1:], x ,acc+1 )
        else:
            return (xs[1:], x, acc)
