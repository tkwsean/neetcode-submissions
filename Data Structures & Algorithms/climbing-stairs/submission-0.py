class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 2, 3
        if n <= 3:
            return n
        for i in range(4, n+1):
            temp = n1+n2
            n1 = n2
            n2 = temp
        return n2