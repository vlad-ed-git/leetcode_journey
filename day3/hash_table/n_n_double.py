class Solution:
    def checkIfExist(self, arr):
        exists = {}
        for num in arr:
            if (num * 2) in exists or ((num / 2) in exists and num % 2 == 0):
                return True
            exists[num] = True
        return False