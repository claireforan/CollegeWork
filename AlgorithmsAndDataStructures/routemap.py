# Claire Foran 115379021
 
class Vertex:
    """ A Vertex in a graph. """
       
    def __init__(self, element):
        """ Create a vertex, with data element. """
        self._element = element
      
    def __str__(self):
        """ Return a string representation of the vertex. """
        return str(self._element)
   
    __repr__ = __str__
      
    def __lt__(self, v):
        return self._element < v.element()
   
    def element(self):
        """ Return the data for the vertex. """
        return self._element
       
class Edge:
    """ An edge in a graph.
   
        Implemented with an order, so can be used for directed or undirected
        graphs. Methods are provided for both. It is the job of the Graph class
        to handle them as directed or undirected.
    """
       
    def __init__(self, v, w, element):
        """ Create an edge between vertice v and w, with label element.
   
            element can be an arbitrarily complex structure.
        """
        self._vertices = (v,w)
        self._element = element
   
    def __str__(self):
        """ Return a string representation of this edge. """
        return ('(' + str(self._vertices[0]) + '--'
                   + str(self._vertices[1]) + ' : '
                   + str(self._element) + ')' )
   
    __repr__ = __str__
   
    def get_start(self):
        return self._time
   
    def get_time(self):
        return self._vertices[0]
   
    def get_end(self):
        return self._vertices[1]
   
    def vertices(self):
        """ Return an ordered pair of the vertices of this edge. """
        return self._vertices
   
    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]
   
    def end(self):
        """ Return the second vertex in the ordered. pair. """
        return self._vertices[1]
   
    def opposite(self, v):
        """ Return the opposite vertex to v in this edge. """
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None
   
    def element(self):
        """ Return the data element for this edge. """
        return self._element
  
from APQ import *
class RouteMap():
    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()
        self._elements = dict()
        self._coordinates = dict()
    
  
    def __str__(self):
        """ Return a string representation of the graph. """
        if self.num_vertices() <= 100 and self.num_edges() <= 100:
            hstr = ('|V| = ' + str(self.num_vertices())
                    + '; |E| = ' + str(self.num_edges()))
            vstr = '\nVertices: '
            for v in self._structure:
                vstr += str(v) + '-'
            edges = self.edges()
            estr = '\nEdges: '
            for e in edges:
                estr += str(e) + ' '
            return hstr + vstr + estr
          
  
      
    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)
  
    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])    #the dict of edges for v
        return num //2     #divide by 2, since each edege appears in the
                           #vertex list for both of its vertices
  
    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]
  
    def get_vertex_by_label(self, element):
        """ get the first vertex that matches element. """
        return self._elements[element]
  
    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                #to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist
  
    def get_edges(self, v):
        """ Return a list of all edges incident on v. """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None
  
    def get_edge(self, v, w):
        """ Return the edge between v and w, or None. """
        if (self._structure != None
                         and v in self._structure
                         and w in self._structure[v]):
            return self._structure[v][w]
        return None
  
    def degree(self, v):
        """ Return the degree of vertex v. """
        return len(self._structure[v])
  
      
    def add_vertex(self, element, latitude, longitude):
          
        v = Vertex(element)
        self._structure[v] = dict()
        self._elements[element] = v
        self._coordinates[v] = (latitude, longitude)
        return v
  
    def add_vertex_if_new(self, element,latitude,longitude):
          
        for v in self._structure:
            if v.element() == element:
                return v
        return self.add_vertex(element, latitude,longitude)
  
    def add_edge(self, v, w, element):
          
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e
  
    def get_vertex_by_label(self, element):
        """ get the first vertex that matches element. """
        return self._elements[element]
              
    def sp(self, v, w):
        table = self.dijktsra(v)
        lst = []
        lst += [(w, table[w][0])]
        while w != v:
            w = table[w][1]
            lst += [(w, table[w][0])]
             
        return lst[::-1]
     
    def dijktsra(self, s):
        openAPQ = APQ()
        locs = {}
        closed = {}
        preds = {s:None}
       
        elt = openAPQ.add(0, s)
        locs[s] = elt
        while not openAPQ.is_empty():
  
            # remove the min element and its key from open
            apq_elt = openAPQ.remove_min()
            vertex = apq_elt._value
              
            # remove the entry for v from locs and from preds
            locs.pop(vertex)
            predecessor = preds.pop(vertex)
              
            # add an entry for v with cost and predecessor into closed
            cost = apq_elt._key
            closed[vertex] = (cost, predecessor)
            for e in self.get_edges(vertex):
                w = e.opposite(vertex)
                if w not in closed:
                    newcost =  cost + e._element
                    if w not in locs:
                        preds[w] = vertex
                        elt = openAPQ.add(newcost, w)
                        locs[w] = elt
                    elif newcost < openAPQ.get_key(locs[w]):
                        preds[w] = vertex
                        # update w's cost in open to newcost
                        openAPQ.update_key(locs[w], newcost)
        return closed
     
    def printvlist(self, table):
        output = "type\tlatitude\tlongitude\telement \tcost\n"
        for item in table:
            output += "W\t%f\t%f\t%f\t%f\n" %(self._coordinates[item[0]][0], self._coordinates[item[0]][1], item[0]._element, item[1])
        print(output)
      
def graphreader(filename):
    """ Read and return the route map in filename. """
    graph = RouteMap()
    file = open(filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        line = (file.readline().split())
        gps = (float(line[1]),float(line[2]))
        vertex = graph.add_vertex(nodeid, gps[0], gps[1])
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = graph.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        time = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, time)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    return graph
  
def test():
    routemap = graphreader('corkCityData.txt')
    ids = {}
    ids['wgb'] = 1669466540
    ids['turnerscross'] = 348809726
    ids['neptune'] = 1147697924
    ids['cuh'] = 860206013
    ids['oldoak'] = 358357
    ids['gaol'] = 3777201945
    ids['mahonpoint'] = 330068634
    sourcestr = 'wgb'
    deststr='neptune'
    source = routemap.get_vertex_by_label(ids[sourcestr])    
    dest = routemap.get_vertex_by_label(ids[deststr])
    tree = routemap.sp(source,dest)
    routemap.printvlist(tree)
test()
