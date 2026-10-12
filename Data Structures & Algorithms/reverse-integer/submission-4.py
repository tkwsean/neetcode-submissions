class Solution:
    def reverse(self, x: int) -> int:
        org = x
        num = str(abs(x))
        res = 0
        reversed_num = int(num[::-1])
        if org > 0:
            res = reversed_num
        elif org < 0:
            res = -reversed_num
        if res < -(2**31) or res > (2**31)-1:
            return 0
        return res
