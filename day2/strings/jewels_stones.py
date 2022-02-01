class Solution:
    ## O(n*2) solution
    def numJewelsInStones(self, jewels, stones):
        count  = 0
        for stone in stones:
            if stone in jewels:
                count = count + 1
        return count
    
    ## O(n+m) solution
    def numJewelsInStones(self, jewels, stones):
        setJewels = set(jewels)
        return sum(s in setJewels for s in stones)