import collections

class Node():
    def __init__(self, value):
        self.value = value #distinct values
        self.links = []#if list is passed in as a variable with a default option then it isn't unique
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
    
    def topological_sort(self):
        que = collections.deque()
        for key in self.nodes.keys():
            self.recursion(self.nodes[key], que)
        return que

    def recursion(self, node: Node, que: collections.deque):
        if not node.visited:
            node.visited = True
            for directed_node in node.links:
                self.recursion(directed_node, que)
            que.appendleft(node.value)


n = 6
#edges = [[1,2],[1,3],[3,4], [2,4]]
edges = [[1,2],[1,3],[2,3],[4,1], [4,5], [5,6], [6,4] ]
node_list = [Node(x) for x in range(1,n+1)]
test_graph = Graph()
for node in node_list:#add nodes to graph
    test_graph.add_node(node)
for a,b in edges:#link nodes in graph
    test_graph.link_nodes(test_graph.nodes[a],test_graph.nodes[b])

print(test_graph.topological_sort())
