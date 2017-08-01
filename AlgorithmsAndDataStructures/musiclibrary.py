class Track(object):
  
    def __init__(self, name, artiste, timesplayed):
        self._name = name
        self._artiste = artiste
        self._timesplayed = timesplayed
  
    def __str__(self):
        return "(%s; %s; %i)" % (self._name, self._artiste, self._timesplayed)
  
    def play(self):
        self._timesplayed += 1
  
   
class DLLNode(object):
    def __init__(self, item, prevnode, nextnode):
        self._element = item
        self._prevnode = prevnode
        self._nextnode = nextnode


class DLList(object):
    def __init__(self):
        self._size = 0
        self._tail = DLLNode('Tail', None, None)
        self._head = DLLNode('Head', None, self._tail)
        self._current = self._head
    def __str__(self):
        return "Size: %i, Current: %s" % (self._size, self._current)
 
    def get_first(self):
        return self._head._nextnode
      
    def add_after(self, item, b_node):
        new_node = DLLNode(item, b_node, self._tail)
        b_node._nextnode._prevnode = new_node
        new_node._nextnode = b_node._nextnode
        new_node._prevnode = b_node
        b_node._nextnode = new_node
        self._size += 1
  
    def add_first(self, item):
        self.add_after(item, self._head)
         
    def add_last(self, item, node):
        self.add_after(item, self._tail._prevnode)
         
    def move_current(self, item, next_node):
  
        self._current = self._current._nextnode
              
    def remove_node(self):
        node = self._current
        self._current = node._nextnode
        node._prevnode._nextnode = node._nextnode
        node._nextnode._prevnode = node._prevnode
        node._nextnode = None
        node._prevnode = None
        node = None
        self._size -= 1
              
    def swapAdjacent(self, node1, node2):
        node1._prevnode._nextnode = node2
        node2._nextnode._prevnode = node1
        node2._prevnode = node1._prevnode
        node1._nextnode = node2._nextnode
        node1.prevnode = node2
        node2._nextnode = node1
        
class MusicLibrary():
  
    def __init__(self, tracks):
        self._tracks = DLList()
 
    def __str__(self):
        strng= ""
        node = self._tracks.get_first()
        print("Tracks:")
        while node != self._tracks._tail:
            if node._element == self.get_current():
                strng += ">>> %s, %s, %i\n" % (node._element._name, node._element._artiste, node._element._timesplayed)
            else:
                strng += "%s, %s, %i\n" % (node._element._name, node._element._artiste, node._element._timesplayed)
            node = node._nextnode
        return strng
     
    def add_track(self, track):
        if self._tracks._size == 0:
            self._tracks.add_first(track)
        else:
            self._tracks.add_last(track, self._tracks._tail)
              
  
    def get_current(self):
        if self._tracks._size == 0:
            return None
        else:
            return self._tracks._current
 
  
    def next_track(self):
        print("Current track: %s" % self._tracks._current._nextnode._element)
        self._tracks._current = self._tracks._current._nextnode

  
    def prev_track(self):
        self._tracks._current = self._tracks._current._prevnode
          
    def reset(self):
        self._tracks._current = get_first()
  
    def play(self):
        self._tracks._current._element.play()
        print("Currently playing: %s" % self._tracks._current._element)
  
    def remove_current(self):
        self._tracks.remove_node()
  
    def sort_by_name(self):
        print("Sorting")
        node = self._tracks.get_first
        print(node._element)
        while node._nextnode != self._tracks._tail:
            print(node._element)
            print(node._nextnode._element)
            
            if node._nextnode._element._name > node._element._name:
                self._tracks.swapAdjacent(node, node._nextnode)
            node = node._nextnode

        print("sorted")
            
        
    
    def sort_by_artiste(self):
        node = self._tracks._head._nextnode
        while node._nextnode != self._tracks._tail:
            if node._nextnode._element._artiste > node._element._artiste:
                self._tracks.swapAdjacent(node, node._nextnode)
            node = node._nextnode
          
  
    def length(self):
        return self._tracks._size

    def search(self, strng):
        node = self.get_current()
        start = self.get_current()
        wrap = False
        # What if current is at head
        while node._nextnode:
            if strng in node._element._name or strng in node._element._artiste:
                self._tracks._current = node
                return True
            elif node == self._tracks._tail:
                wrap = True
                node = self._tracks.get_first()
            elif node._nextnode == start and wrap:
                print("False")
            else:
                node = node._nextnode

    
  
def main():
    library1 = MusicLibrary(DLList())
    track1 = Track("Say you won't let go", "James Arthur", 0)
    library1.add_track(track1)
    track2 = Track("The Greatest", "Sia feat Kendrick Lamar", 0)
    library1.add_track(track2)
    track3 = Track("Closer", "The Chainsmokers feat Halsey", 0)
    library1.add_track(track3)
    library1.next_track()
    print(library1)
    #library1.sort_by_name()
    
    #print(library1.search("Thx"))
    
    library1.next_track()
    library1.play()
    print(library1.get_current())
    library1.next_track()
    print(library1.get_current())
    library1.play()
    library1.next_track()
    print(library1.get_current())
    library1.prev_track()
    print(library1.get_current())
    
    library1.prev_track()
    print(library1.get_current())

    library1.play()
    print("REMOVING TRACK")
    library1.remove_current()
    print(library1.get_current())
    print(library1)
    
    track4 = Track("My way", "Calvin Harris", 0)
    library1.add_track(track4)
    print(library1)
    
    #library1.sort_by_name()
    print(library1)
    
    library1.prev_track()
    #library1.play()
    print(library1)

      
  
if __name__ == "__main__":
    main()
