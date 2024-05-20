# parse_hw.py by Nishan Maharjan (nmaharjan@csus.edu) for CSC 135 Spring 2024
class scanner:
    # toks[i] must evaluate to the i-th token in the token stream.
    # Assumes toks does not change during parsing
    def __init__(self,toks):
        self._toks = toks
        self._i = 0
    
    # If no more tokens exist or current token isn't s, raise exception.
    # Otherwise pass over the current one and move to the next.
    def match(self,s):
        if (self._i < len(self._toks)) and (self._toks[self._i] == s):
            self._i += 1
        else:
            raise Exception
            
    # If any tokens remain return the current one. If no more, return None.
    def next(self):
        if self._i < len(self._toks):
            return self._toks[self._i]
        else:
            return None


# Input can be any type where len(input) is defined and input[i] yields a
# string (ie, string, list, etc). Raises Exception on a parse error.
# S → <AB
# A → aAb | b
# B → bB | >
def parse1(input):
    toks = scanner(input)
    stack = ['S']
    while len(stack) > 0:
        top = stack.pop() # Always pop top of stack
        tok = toks.next() # None indicates token stream empty
        if tok == top: # Matching stack top to token 
            toks.match(tok)
        elif top == 'S' and tok == '<':  # S -> <AB must be the next  # S -> <
            stack.append('B') # production to follow here
            stack.append('A')
            stack.append('<')
        elif top == 'A' and tok == 'a':  # A -> aAb must be the next
            stack.append('b')            # production to follow here
            stack.append('A')
            stack.append('a')
        elif top == 'A' and tok == 'b':  # A -> b must be the next
            stack.append('b')   
        elif top == 'B' and tok == 'b':  # S -> bB must be the next
            stack.append('B')            # production to follow here
            stack.append('b')
        elif top == 'B' and tok == '>':  # S -> > must be the next
            stack.append('>')            # production to follow here 
        else:
            raise Exception    # Unrecognized top/tok combination
    if toks.next() != None:
        raise Exception


# Input can be any type where len(input) is defined and input[i] yields a
# string (ie, string, list, etc). Raises Exception on a parse error.
# S → BA
# A → +BA | -BA | λ
# B → DC
# C → *DC | /DC | λ
# D → a | (S)
def parse2(input):
    toks = scanner(input)
    stack = ['S']
    while len(stack) > 0:
        top = stack.pop()  # Always pop top of stack
        tok = toks.next()  # None indicates token stream empty
        if tok == top:     # Matching stack top to token
            toks.match(tok)
        elif top == 'A' and tok == None: # next == $ 
            pass
        elif top == 'C' and tok == None: # next == $ 
            pass
        elif top == 'S' and tok in ('a', '('):  # S -> BA must be the next
            stack.append('A')            # production to follow here
            stack.append('B') 
        elif top == 'A' and tok == '+':  # A -> +BA must be the next
            stack.append('A')            # production to follow here
            stack.append('B')
            stack.append('+')
        elif top == 'A' and tok == '-':  # A -> -BA must be the next
            stack.append('A')            # production to follow here
            stack.append('B')
            stack.append('-')
        elif top == 'B' and tok in  ('a','('):  # B -> DC must be the next
            stack.append('C')            # production to follow here
            stack.append('D')
        elif top == 'C' and tok == '*':  # C -> *DC must be the next
            stack.append('C')            # production to follow here
            stack.append('D')
            stack.append('*')
        elif top == 'C' and tok == '/':  # C -> /DC must be the next
            stack.append('C')            # production to follow here
            stack.append('D')
            stack.append('/')
        elif top == 'D' and tok == 'a':  # D -> a must be the next
            stack.append('a')            # production to follow here
        elif top == 'D' and tok == '(':  # D -> (S) must be the next
            stack.append(')')            # production to follow here
            stack.append('S')
            stack.append('(')            # production to follow here
        else:
            raise Exception    # Unrecognized top/tok combination
    if toks.next() != None:
        raise Exception


# The following is a trick to make this testing code be ignored
# when this file is being imported, but run when run directly
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    try:
        parse1("aabxbaa")
    except:
        print("Reject")
    else:
        print("Accept")
    
    try:
        parse2("aabxbaa")
    except:
        print("Reject")
    else:
        print("Accept")

