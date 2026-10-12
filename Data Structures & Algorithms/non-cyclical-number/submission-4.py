def squareNumber(n: int) -> int:
    n = str(n)
    res = 0
    for i in range(len(n)):
        res += int(n[i])**2
    return res

class Solution:
    def isHappy(self, n: int) -> bool:
        isVisited = set()
        squared = squareNumber(n)
        while squared != 1:
            if squared in isVisited:
                return False
            else:
                isVisited.add(squared)
                squared = squareNumber(squared)
        return True
        
        