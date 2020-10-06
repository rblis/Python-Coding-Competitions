class node(object):
    weight = None
    parent = None
    children = []
    visisted = False
    def __init__(self, weight, children=[]):
        super().__init__()
        self.weight = weight
        self.parent = parent
        self.children = children
    
    def add_child(self, child):
        child.parent = self
        self.children.apped(child)
        
    def set_visited(self, visited):
        self.visisted = visisted

class tree(object):
    num_nodes = None
    root = None
    def __init__(self, root):
        self.num_nodes = 0
        self.root = root

    

    
    