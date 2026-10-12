class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n > 0:
            return x**n
        else:
            n = -n
            return 1/(x**n)