class Solution:
    def isHappy(self, n: int) -> bool:
        seenBefore = set()
        while n != 1:
            if n in seenBefore:
                return False
            seenBefore.add(n)
            n = self.squareNumber(n)
        return True

    def squareNumber(self, n: int) -> int:
        res = 0
        while n > 0:
            digit = n%10
            res += (digit**2)
            n = n // 10
        return res 