class BSTNode:
    """ An internal node in a (doubly linked) binary search tree. """
       
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None
   
    def __str__(self):
        """ Return a string representation of the tree rooted at this node.
   
            The string will be created by an in-order traversal.
        """
        return self.inorder()
           
    def inorder(self):
           
        if self._leftchild or self._rightchild:
            outstr = ''
            if self._leftchild:
                outstr += str(self._leftchild.inorder()) + ','               
            outstr += str(self._element) 
            if self._rightchild:
                outstr += ',' + str(self._rightchild.inorder()) 
        else:
            return str(self._element)
        return outstr
      
           
   
    def _statistics(self):
        """ Return a string of the basic statistics for the tree. """
        if self != None:
            return ('size = ' + str(self.size()) + '; height = ' + str(self.height()))    
     
    def search(self, item):
        """ Return the first subtree containing item, or None. """
        if self._element == item:
            return self
        elif self._element >item:
            if self._leftchild:
                if item < self._element:
                    return self._leftchild.search(item)
             
        elif self._element < item:
            if self._rightchild:
                if item > self._element:
                    return self._rightchild.search(item)
        else:
            return None
           
    def add(self, item):
        """ Add item to the tree, maintaining BST properties.
            Note: if item is already in the tree, this does nothing.
        """
        if item < self._element:
            if self._leftchild == None:
                new_node = BSTNode(item)
                self._leftchild = new_node
                new_node._parent = self
            else:
                self._leftchild.add(item)
        elif item > self._element:
            if self._rightchild == None:
                new_node = BSTNode(item)
                self._rightchild = new_node
                new_node._parent = self
            else:
                self._rightchild.add(item)
           
           
    def findmin(self):
        """ Return the minimal element below this node. """
        return self._findminnode()._element
          
       
    def _findminnode(self):
        """ Return the BSTNode with the minimal element below this node. """
        if self._leftchild:
            return self._leftchild._findminnode()
        else:
            return self
   
    def findmax(self):
        """ Return the maximal element below this node. """
        return self._findmaxnode()._element
   
    def _findmaxnode(self):
        """ Return the BSTNode with the maximal element below this node. """
        if self._rightchild:
            return self._rightchild._findmaxnode()
        else:
            return self
       
    def height(self):
        """ Return the height of this node.
   
            Note that with the recursive definition of the tree the height
            of the node is the same as the depth of the tree rooted at this
            node.
       """
         
        if self == None:
            return 0
        elif self.full():
            return 1 + max(self._leftchild.height(), self._rightchild.height())
        elif self._leftchild:
            return 1 + self._leftchild.height()
        elif self._rightchild:
            return 1 + self._rightchild.height()
        else:
            return 0
              
    def size(self):
        """ Return the size of this subtree.
   
            The size is the number of nodes (or elements) in the tree.
        """
        if self == None:
            return 0
          
        elif self.leaf():
            return 1
        else:
            if self.full():
                return 1 + self._leftchild.size() + self._rightchild.size()
            elif self._leftchild:
                return 1 + self._leftchild.size()
            elif self._rightchild:
                return 1 + self._rightchild.size()
                  
    def leaf(self):
        """ Return True if this node has no children. """
        return self._leftchild == None and self._rightchild == None
          
   
    def semileaf(self):
        """ Return True if this node has exactly one child. """
        return not self.leaf() and not self.full()
 
    def full(self):
        """ Return true if this node has two children. """
        return self._leftchild != None and self._rightchild != None
            
    def internal(self):
        """ Return True if this node has at least one child. """
        return self._leftchild != None or self._rightchild != None
          
   
    def remove(self, item):
        """ Remove and return item from the tree rooted at this node.
   
            Maintains the BST properties.
        """
        node = self.search(item)
        if node:
            return node._remove_node()
        else:
            return "This does not exist in the tree"
        
                   
   
    def _remove_node(self):
        """ (Private) Remove this BSTBode from its tree.
   
            Maintains the BST properties.
        """
        old = self
        if self.full():
            biggest = self._leftchild._findmaxnode()
            self._element = biggest._element
            if self._parent:
                if biggest._leftchild:
                    biggest._pullup(biggest._leftchild)               
                else:
                    biggest._remove_node()               

        elif self.leaf():
            old = self
            if self._parent:
                 
                if self == self._parent._leftchild:
                    self._parent._leftchild = None
                elif self == self._parent._rightchild:
                    self._parent._rightchild = None
                self._element = None
                self._parent = None
                 
            else:
                self = None


        elif self._rightchild == None:
            if self._parent:
                self._pullup(self._leftchild)
            else:
                self._element = self._leftchild._element
                self._leftchild._element = None
                self._leftchild = None
                self._leftchild._parent = None

                
        elif self._leftchild == None:
            if self._parent:
                self._pullup(self._rightchild)
            else:
                self._element = self._rightchild._element
                self._rightchild._element = None
                self._rightchild._parent = None
                self._rightchild = None
       
        return old._element
        
       
   
    def _pullup(self, node):
        """ Pull up the child tree rooteed at node into this BSTNode. """
        element = self._element
        if self == self._parent._leftchild:
            self._parent._leftchild = node
        else:
            self._parent._rightchild = node
        node._parent = self._parent
        self._rightchild = None
        self._leftchild = None
        self._parent = None
        self._element = None
        self = node
        return element

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        outstr = str(self._element) + '(' + str(self.height()) + ')['
        if self._leftchild:
            outstr = outstr + str(self._leftchild._element) + ' '
        else:
            outstr = outstr + '* '
        if self._rightchild:
            outstr = outstr + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '*]'
        if self._parent:
            outstr = outstr + ' -- ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- *'
        print(outstr)
        if self._leftchild:
            self._leftchild._print_structure()
        if self._rightchild:
            self._rightchild._print_structure()
   
    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False       
        if self._parent:
            if (self._parent._leftchild != self
                and self._parent._rightchild != self):
                ok = False
        return ok
       
    def _testadd():
        node = BSTNode('mushroom')
        node._print_structure()
        print('adding green bean')
        node.add('green bean')
        node._print_structure()
        print('adding radish')
        node.add('radish')
        node._print_structure()
        print('adding pea')
        node.add('pea')
        node._print_structure()
        print('adding pepper')
        node.add('pepper')
        node._print_structure()
        print('adding parsnip')
        node.add('parsnip')
        node._print_structure()
        print( node)
        print(node.search('pea'))
        print(node.findmin())
        print(node._findminnode())
        print(node.findmax())
        print(node._findmaxnode())
        print(node.size())
        print(node.leaf())
        print(node.semileaf())
        print(node.full())
        print(node.internal())
        print(node.remove('raddish'))
         
    def _new_test():
        c= BSTNode('apple')
        c.add('grape')
        c.add('mango')
        c.add('banana')
        c.add('carrot')
        print(c)
        print(c.remove('gape'))
        
        c._print_structure()
        print(c)
         
         
         
    def _test():
        node = BSTNode(1)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 0)
        node.add(0)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 0)
        node.remove(0)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 2)
        node.add(2)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 2)
        node.remove(2)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 6)
        node.add(6)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 1)
        node.remove(1)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 2)
        node.add(2)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 4)
        node.add(4)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 3)
        node.add(3)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 5)
        node.add(5)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 2)
        node.remove(2)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 4)
        node.remove(4)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 3)
        node.remove(3)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 5)
        node.remove(5)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 12)
        node.add(12)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 8)
        node.add(8)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 9)
        node.add(9)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 7)
        node.add(7)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 12)
        node.remove(12)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 8)
        node.remove(8)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 9)
        node.remove(9)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 7)
        node.remove(7)
        print('Ordered:', node)
        node._print_structure()
        
   
   
import re

def wordbst(filename):
    file = open(filename, "r")  #open the file
    output = open("output.txt", "w")
    fulltext = file.read()         #read it all into one big string
    stripped = re.sub("[^a-zA-Z\s]+", "", fulltext)  #remove non-letters or -spaces
    lowercase = stripped.lower()            #convert all to lower case
    wordlist = lowercase.split() #split the string on white space into words in a list
    print(len(wordlist), "words in total")
    bst = BSTNode(wordlist[0])
    for word in wordlist:
        bst.add(word)
    bst._print_structure()
    print('Number of unique words:', bst.size())
    
    print(bst.height())
    
    node = bst.search('election')
    print(node._statistics())
    print(node)
    
    node = bst.search('president')
    print(node._statistics())
    print(node)
    
    node = bst.search('country')
    print(node._statistics())
    print(node)
    
    node = bst.search('liberty')
    print(node._statistics())
    print(node)
    
    node = bst.search('democracy')
    print(node._statistics())
    print(node)
    
    
    return bst
  
if __name__=="__main__":
    wordbst('lincoln.txt')
