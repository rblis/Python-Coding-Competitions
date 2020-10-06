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

    def depth_first_search(self, root):
        que = collections.deque()
        root.visited = True
        root.value = float("inf")
        que.append(root)
        dfs = []
        while que:
            pop_node = que.pop()
            dfs.append(pop_node.value)
            for adj_node in pop_node.links:
                if not adj_node.visited:
                    adj_node.visited = True
                    adj_node.distance += pop_node.distance + 6
                    que.append(adj_node)
        return dfs

def dfs(n, m, edges, s):
    node_list = [Node(x) for x in range(1,n+1)]
    test_graph = Graph()
    for node in node_list:
        test_graph.add_node(node)
    for a,b in edges:
        test_graph.link_nodes(test_graph.nodes[a],test_graph.nodes[b])
    print(test_graph.depth_first_search(test_graph.nodes[s]))
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

print(dfs(5,3,[[1,2],[1,3],[3,4]], 1))

x = set()
x.add(1)
x.add(4)
x.add(3)
print(x)