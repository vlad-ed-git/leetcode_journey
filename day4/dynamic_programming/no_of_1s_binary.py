"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10 


"""
# TIP dec to binary ==> divide by 2 until quotient is zero e.g. 1/2 = 0 remain 1 ...and collect remainders from start i.e. in reverse 
## O(n log n) solution
class Solution:
    def noOf1sInBinary(self, num, noOf1s = 0):
        quotient = int(num / 2)
        remainder = (num % 2)
        if remainder == 1:
            noOf1s = noOf1s + remainder
        if quotient == 0:
            return noOf1s
        else:
            return self.noOf1sInBinary(quotient, noOf1s)
            
    def countBits(self, n):
        ans = []
        i = 0
        while i <= n:
            ones = self.noOf1sInBinary(i)
            ans.append(ones)
            i = i + 1
        return ans
    

"""
To understand the solution, we remember the following two points from math:

All whole numbers can be represented by 2N (even) and 2N+1 (odd).
For a given binary number, multiplying by 2 is the same as adding a zero at the end (just as we just add a zero when multiplying by ten in base 10).
Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's. Likewise, doubling a number and adding one will increase the count by exactly 1. Or:

countBits(N) = countBits(2N)
countBits(N)+1 = countBits(2N+1)
Thus we can see that any number will have the same bit count as half that number, with an extra one if it's an odd number. We iterate through the range of numbers and calculate each bit count successively in this manner:
"""
# O(n) solution which I do not understand
class Solution:            
    def countBits(self, n: int):
        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[int(i / 2)] + i % 2)
        return counter