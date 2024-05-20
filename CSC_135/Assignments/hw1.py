def contains(self, item):
    if self._item == item:
        hasheditem = hash(item) 
        childnum = hasheditem % hamt.DEG  # bottom two bits
        if self._children[childnum] == None:
            return False
        else:
            shiftedhashbits = hasheditem // hamt.DEG
            newsearch = self._children[childnum].contains(shiftedhashbits)
            if newsearch == None:
                return True
            else:
                False


def __iter__(self):
        return HamtIter(self)
    

class HamtIter:
    
    # Iterator needs to know how to start
    def __init__(self, firstitem):
        self._curitem = firstitem 
        
    def __next__(self):
        if self._curitem._children == None:
            raise StopIteration
        else:
            tmp = self._curitem._item
            self._curitem = self._curitem._children 
            return tmp
