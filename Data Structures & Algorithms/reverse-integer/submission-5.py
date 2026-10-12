class Solution:
    def reverse(self, x: int) -> int:
        absNum = abs(x)
        isNegative = x < 0
        strNum = str(absNum)
        reversedNum = strNum[::-1]
        if int(reversedNum) < -2**31 or int(reversedNum) > (2**31)-1 or int(reversedNum) == 0:
            return 0
        elif isNegative:
            return -1*int(reversedNum)
        else:
            return int(reversedNum)