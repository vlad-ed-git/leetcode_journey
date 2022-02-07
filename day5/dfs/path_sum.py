"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""

def hasPathSum( root, targetSum):
    if root is None:
        return False;
    if root.left is None and root.right is None:
        return targetSum - root.val == 0
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return 0
   
        stack = [[root, root.val]]      
        while len(stack) > 0:
            node, sumSoFar = stack.pop()
        
            if node.right:
                    stack.append([node.right, sumSoFar + node.right.val])

            if node.left:
                    stack.append([node.left, sumSoFar + node.left.val])

            if node.left is None and node.right is None:
                    # we have a leaf
                    if sumSoFar == targetSum:
                        return True
                    
        return False