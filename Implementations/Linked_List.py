class LinkNode():
    def __init__(self, val=0, left=None, right=None):
        super().__init__()
        self.val = val
        self.left = left
        self.right = right
        
def swap(nodeA, nodeB):
    nodeA.right = nodeB.right
    nodeB.left = nodeA.left
    nodeA.left.right = nodeB
    nodeB.right.left = nodeA
    nodeA.left = nodeB
    nodeB.right = nodeA