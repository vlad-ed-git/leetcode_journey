# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        """recursive --> return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1 """
        
   
        stack = [[root, 1]] # node and depth
        depth = 1 # we know we have at least 1 node i.e. root
        maxDepth = 1
        while len(stack) > 0:
            node, depth = stack.pop()
            if node.right:
                stack.append([node.right, depth + 1])
            if node.left:
                stack.append([node.left, depth + 1])
            maxDepth = max(maxDepth, depth)
        return  maxDepth