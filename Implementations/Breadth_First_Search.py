'''
Undirected Graph
'''
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
    #Modify later to incorporate seperate Edge objects 
    def link_nodes(self, nodeA, nodeB):
        if nodeA.value in self.nodes.keys() and nodeB.value in self.nodes.keys():
            self.nodes[nodeA.value].add_link(nodeB)
            self.nodes[nodeB.value].add_link(nodeA)

    def breadth_first_search(self, root):
        que = collections.deque()
        root.visited = True
        root.value = float("inf")
        que.append(root)
        #bfs = []
        while que:
            pop_node = que.popleft()
            #bfs.append(pop_node)
            for adj_node in pop_node.links:
                if not adj_node.visited:
                    adj_node.visited = True
                    adj_node.distance += pop_node.distance + 6
                    que.append(adj_node)
        #return bfs

def bfs(n, m, edges, s):
    node_list = [Node(x) for x in range(1,n+1)]
    test_graph = Graph()
    for node in node_list:#add nodes to graph
        test_graph.add_node(node)
    for a,b in edges:#link nodes in graph
        test_graph.link_nodes(test_graph.nodes[a],test_graph.nodes[b])
    test_graph.breadth_first_search(test_graph.nodes[s])
    result = [0]*(n)
    for key in test_graph.nodes.keys():
        node = test_graph.nodes[key]
        if node.visited == False:
            result[key-1] = -1
        else:
            if node.value == s:
                pass
            else:
                result[key-1] = node.distance
    result.pop(s-1)
    
    return result

bfs(5,3,[[1,2],[1,3],[3,4]], 1)


# test_graph = Graph()
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# test_graph.add_node(node1)
# test_graph.add_node(node2)
# test_graph.add_node(node3)
# test_graph.add_node(node4)
# test_graph.add_node(node5)
# test_graph.link_nodes(node1,node2)
# test_graph.link_nodes(node1,node3)
# test_graph.link_nodes(node3,node4)
# print(test_graph.breadth_first_search(node1))


'''
Not optimized

class Node():
    def __init__(self, value):
        self.value = value #distinct values
        self.links = list()
        self.distance = 0
        self.visited = False

    def add_link(self, new_link):
        if new_link not in self.links:
            self.links.append(new_link)
            #self.links.sort()

class Graph():
    
    def __init__(self):
        self.nodes = {}
    def add_node(self, new_node: Node):
        if isinstance(new_node, Node) and new_node.value not in self.nodes:
            self.nodes[new_node.value] = new_node
            return True
        else:
            return False
    def link_nodes(self, start, end):
        if start.value in self.nodes.keys() and end.value in self.nodes.keys():
            complete = 0
            for key, value in self.nodes.items():
                if key == start.value:
                    value.add_link(end)
                    complete += 1
                if key == end.value:
                    value.add_link(start)
                    complete += 1
                if complete ==2:
                    return True
        else:
            return False
    
    def breadth_first_search(self, start: Node):
        que = collections.que()
        print(start.value, start.distance)
        start.distance = 0
        start.visited = True
        distance = 1
        for link in start.links:
            self.nodes[link.value].ditance = start.distance + distance
            que.append(link)
        while len(que) > 0:
            explore_node = que.popleft()
            explore_node.visited = True
            print(explore_node.value, explore_node.distance)
            for temp_node in explore_node.links:
                if(temp_node.visited == False):
                    que.append(temp_node)
                    if temp_node.distance > explore_node.distance + distance:
                        temp_node.distance = explore_node.distance+distance


'''




