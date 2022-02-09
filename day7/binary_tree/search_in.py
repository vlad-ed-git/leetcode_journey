class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.val == val:
                return node
            elif node.val < val:
                #ignore left branch      
                if node.right:
                    if node.right.val == val:
                        return node.right
                    stack.append(node.right)
            else:
                # ignore right branch
                if node.left:
                    if node.left.val == val:
                        return node.left
                    stack.append(node.left)
        return None