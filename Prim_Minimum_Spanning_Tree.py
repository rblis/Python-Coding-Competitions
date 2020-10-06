class Node():
    def __init__(self, value):
        self.value = value
        self.links = []
        self.visisted = False
        self.distance = 0

    def add_link(self, link: Link):
        if link not in links:
            links.append(link)


class Link():
    def __init__(self, start_node: Node, end_node: Node, distance):
        self.start_node = start_node
        self.end_node = end_node
        self.distance = distance

class Graph():
    nodes = {}
    links = []
    def __init__(self):
        1
    
    def add_node(self, node: Node):
        if node.value not in nodes.keys:
            nodes[node.value] = node
    
    def add_link(self, link: Link):
        links.append(link)
        nodes[link.start_node.value].append(link)
        nodes[link.end_node.value].append(link)