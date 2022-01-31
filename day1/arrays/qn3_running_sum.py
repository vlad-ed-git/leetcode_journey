"""
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

"""
class Solution:
    def runningSum(self, nums):
        prev = nums[0]
        ans = []
        for index, val  in enumerate(nums):
            if index == 0:
                ans.append(val)
            else:
                aSum = prev+val
                ans.append(aSum)
                prev = aSum
        return ans