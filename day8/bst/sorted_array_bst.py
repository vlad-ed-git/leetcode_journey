#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        #base cases
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        #simplest case e.g. [1,2,3]
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        if (mid - 1) >= 0:
            node.left = self.sortedArrayToBST(nums[:mid])
        if (mid + 1) <= len(nums):
            node.right = self.sortedArrayToBST(nums[mid+1:])
        #greater cases
        #repeat with partitions 
        return node
        
            
        