'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        inorder = []
        node: TreeNode = root
        while(node != None or len(stack) != 0):
            while(node != None):
                stack.append(node)
                node = node.left
            node = stack.pop(len(stack)-1)
            inorder.append(node.val)
            node = node.right
        return inorder
