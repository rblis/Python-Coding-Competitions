class tree_node(object):
    
    def __init_(self, parent = None, left = None, right = None, data = None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data

class binary_tree(object):

    def __init__(self, root):
        self.root = root
        self.num_nodes = 0

    def insert(self, new_node):
        node = self.root
        inserted = False
        while(not inserted):
            if(new_node.data >= node.data): #insert to the right subtree
                if(node.right == None):
                    node.right = new_node
                    self.num_nodes +=1
                    inserted = True
                else:
                    node = node.right
            else:
                if(node.left == None):
                    node.left = new_node
                    self.num_nodes +=1
                    inserted = True
                else:
                    node = node.left


    
        

