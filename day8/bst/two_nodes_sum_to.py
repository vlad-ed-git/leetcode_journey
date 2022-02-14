#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        stack = []
        visitedNodes = {}
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if (k - node.val) in visitedNodes:
                return True
            visitedNodes[node.val] = True # visited
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False
            
        