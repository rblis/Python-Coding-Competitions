'''
Undirected Graph
'''
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