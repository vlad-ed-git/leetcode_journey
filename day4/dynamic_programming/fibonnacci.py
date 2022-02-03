class Solution:
    def fibO2PowN(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
        def fibOofN(self, n):
            if n <= 1:
                return n
            else:
                a = 0
                b = 1
                sumF = 0
                # fib @4 is 3 i.e. => (0+1) , (1+1),  (2+1) = 1, 2, 3
                while n > 1:
                    sumF = a + b
                    a = b
                    b = sumF    
                    n = n - 1
                return sumF