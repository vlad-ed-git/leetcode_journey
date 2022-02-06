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

## TODO understand and try iterative