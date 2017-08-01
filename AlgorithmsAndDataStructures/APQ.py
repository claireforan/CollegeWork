class Element:
    """ A key, value and index. """
  
    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i
    def __eq__(self, other):
        return self._key == other._key
     
    def __lt__(self, other):
        return self._key < other._key
     
    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None
 
    def __str__(self):
         
        return ("(K: %i, V: %s, I: %i)" %(self._key, self._value, self._index))
 
    __repr__ = __str__
  
class APQ:
  
    def __init__(self):
        self._heap = []
    
    def __str__(self):
        strng = ""
        for i in range(len(self._heap)):
            strng += ("Key: %i, Value: %s, Index: %i \n") %(self._heap[i]._key, self._heap[i]._value, i)
 
        return strng
     
    __repr__ = __str__
             
    def bubbleUp(self, element):
        e = element._index
        p = (e-1)//2
        parent = self._heap[p]
        if p < len(self._heap)-1 and p >= 0:
            if self._heap[e]._key < self._heap[p]._key:
                self.swap(element, self._heap[p])
                self.bubbleUp(element)
             
    def bubbleDown(self, element):
        e = element._index
        lefti = 2*element._index + 1
        righti = 2*element._index + 2
        if (lefti < len(self._heap)) and (righti < len(self._heap)):
            if self._heap[lefti]._key < self._heap[righti]._key:
                if element._key > self._heap[lefti]._key:
                    self.swap(element, self._heap[lefti])
                    self.bubbleDown(element)
            else:
                if element._key > self._heap[righti]._key:
                    self.swap(element, self._heap[righti])
                    self.bubbleDown(element)
                 
        elif lefti < len(self._heap):
            if element._key > self._heap[lefti]._key:
                self.swap(element, self._heap[lefti])
                self.bubbleDown(element)
             
        elif righti < len(self._heap):
            if element._key > self._heap[righti]._key:
                self.swap(element, self._heap[righti])
                self.bubbleDown(element)
             
         
         
    def add(self, key, item):
        element = Element(key, item, len(self._heap))
        self._heap += [element]
        self.bubbleUp(element)
        return element
      
    def _min(self):
        return self._heap[0]._value
         
    def remove_min(self):
        minElement = self._heap[0]
        if len(self._heap) == 1:
            self._heap.pop()
        else:
            self._heap[0] = self._heap[len(self._heap)-1]
            self._heap[0]._index = 0
            self._heap.pop()
            self.bubbleDown(self._heap[0])
        return minElement
         
    def swap(self, element1, element2):
        i1 = element1._index
        i2 = element2._index
        self._heap[i1] = element2
        self._heap[i2] = element1
        element1._index = i2
        element2._index = i1

        
    def is_empty(self):
        if self.length() == 0:
            return True
        return False
  
    def length(self):
        return len(self._heap)
  
    def update_key(self, element, newkey):
        e = element._index
        element._key = newkey
        left = 2*e + 1
        right = 2*e + 2
        p = (e-1)//2
        if self._heap[e]._key < self._heap[p]._key:
            self.bubbleUp(self._heap[e])
        elif (left < len(self._heap)) or (right < len(self._heap)):
            self.bubbleDown(self._heap[e])
  
    def get_key(self, element):
        return element._key
  
    def remove(self, element):
        if element == self._heap[0]:
            self.remove_min()
        elif element == self._heap[-1]:
            self._heap.pop()
        else:
            e = element._index
            left = 2*e + 1
            right = 2*e + 2
            p = (e-1)//2
            last = len(self._heap)-1
            self._heap[e],self._heap[last] = self._heap[last], self._heap[e]
            self._heap[e]._index = e
            self._heap.pop(last)
            if self._heap[e]._key < self._heap[p]._key:
                self.bubbleUp(self._heap[e])
            elif (left < len(self._heap)) or (right < len(self._heap)):
                self.bubbleDown(self._heap[e])
        
   

