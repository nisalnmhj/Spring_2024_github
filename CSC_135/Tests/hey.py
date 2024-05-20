from List135 import rest

def num_greater(xs, x):
    return _num_greater(xs, x, 0)

def _num_greater(xs, x, acc):
    if xs.empty():
        return acc
    else:
        if acc > x:
            return _num_greater (xs.rest(), x, acc + 1)
        else:
            return _num_greater (xs.rest(), x, acc)
        
        
'''
def _num_greater(xs, x, acc):
    if xs.empty():
        return acc
    else:
        if acc > x:
            return (xs.rest(), x, acc + 1)
        else:
            return (xs.rest(), x, acc)
'''