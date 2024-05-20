class List135:
    
    # create new list node. Defaults to a node representing the empty list
    def __init__(self, initdata=None, initnext=None):
        self._data = initdata
        self._next = initnext
    
    # is the list beginning with self the end of the list?
    def empty(self):
        return self._next == None
    
    # return the first element of the list that starts with self
    def first(self):
        return self._data
    
    # return the list that begins after the list that starts with self
    def rest(self):
        return self._next
    
    # return a list beginning with data, followed by list beginning with self
    def add(self, data):
        return List135(data, self)
    
    # tail-recursively accumulates "," + str(cur._data) for each remaining item
    def _str(self, cur, acc):
        if cur._next == None:
            return acc
        else:
            nextacc = acc + "," + str(cur._data)
            nextcur = cur._next
            return self._str(nextcur, nextacc)
    
    def __str__(self):
        if self._next == None:
            return "[]"
        else:
            acc = str(self._data)   # init accumulator with first item
            cur = self._next        # continue accumulation with next
            return "[" + self._str(cur, acc) + "]"
