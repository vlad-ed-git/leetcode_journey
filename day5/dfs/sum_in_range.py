""" 
QN.

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

""" 
## O(V) -- v == visited 
# Definition for a binary tree node. 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    def searchDFSRecursively(self, node, searchFor):
        while node is not None:
            if searchFor == node.val:
                print("found") 
                break
            else:
                self.searchDFSRecursively(node.right, searchFor)
                self.searchDFSRecursively(node.left, searchFor)
            
    def searchDFS(self, node, searchFor):
        #list as stack
        stack = []
        stack.append(node) #push 1st in -- last out
        while len(stack) > 0:
            node = stack.pop() # get the last item in
            if node is not None:
                if searchFor == node.val:
                    print("found") 
                    break
                else:
                    stack.append(node.right, searchFor)
                    stack.append(node.left, searchFor)
                
    def searchBFS(self, node, searchFor):
        #list as queue
        queue = []
        queue.append(node) #push 1st in -- first out
        while len(queue) > 0:
            node = queue.pop(0) # get the first item in
            if node is not None:
                if searchFor == node.val:
                    print("found") 
                    break
                else:
    
                    queue.append(node.right, searchFor)
                    queue.append(node.left, searchFor)

            
    
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int):
        # because it is a binary search tree and each is unique
        # at a node, if node is less than low, ignore left branch
        # at a node, if node is greater than high, ignore right branch
        node = root
        if node is None:
            return 0
        if node.val < low:
            return self.rangeSumBST(node.right, low, high)
        elif node.val > high:
            return self.rangeSumBST(node.left, low, high)
        else:
            return node.val + self.rangeSumBST(node.left, low, high) + self.rangeSumBST(node.right, low, high)
        
        """ ITERATIVE METHOD
        stack = []
        stack.append(root)
        sumOf = 0
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                if node.val < low:
                    if node.right is not None:
                        stack.append(node.right)
                elif node.val > high:
                    if node.left is not None:
                        stack.append(node.left)
                else:
                    sumOf = sumOf + node.val
                    if node.right is not None:
                        stack.append(node.right)
                    
                    if node.left is not None:
                        stack.append(node.left)
        return sumOf """
        
        