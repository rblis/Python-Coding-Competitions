import collections
class Node():
    def __init__(self, value):
        self.value = value #distinct values
        self.links = []#if list is passed in as a variable with a default option then it isn't unique
        self.distance = 0
        self.visited = False

    def add_link(self, new_link):
        if new_link not in self.links:
            self.links.append(new_link)
class Graph():
    def __init__(self):
        self.nodes: dict[object,Node] = {}

    def add_node(self, new_node):
        if new_node.value not in self.nodes:
            self.nodes[new_node.value] = new_node
            return True
        else:
            return False
    #Directed Linking
    def link_nodes(self, nodeA, nodeB):
        if nodeA.value in self.nodes.keys() and nodeB.value in self.nodes.keys():
            self.nodes[nodeA.value].add_link(nodeB)

    def depth_first_search(self):
        que = collections.deque()
        dfs = []
        visiting_set = set()
        for unvisited in self.nodes.keys():
            if not self.nodes[unvisited].visited:
                self.nodes[unvisited].visited = True
                que.append(self.nodes[unvisited])                
                while que:
                    pop_node = que.pop()
                    if pop_node.visited and len(que) > 0:
                        return False
                    dfs.append(pop_node.value)
                    for adj_node in pop_node.links:                        
                        if not adj_node.visited:
                            adj_node.visited = True
                            que.append(adj_node)                        
        return True
        

n = 6
edges = [[1,2],[1,3],[2,3],[4,1], [4,5], [5,6], [6,4] ]

node_list = [Node(x) for x in range(1,n+1)]
test_graph = Graph()
for node in node_list:#add nodes to graph
    test_graph.add_node(node)
for a,b in edges:#link nodes in graph
    test_graph.link_nodes(test_graph.nodes[a],test_graph.nodes[b])
print(test_graph.depth_first_search())
