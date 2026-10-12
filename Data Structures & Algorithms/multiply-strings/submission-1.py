class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0]*(len(num1)+len(num2))
        reversedOne = num1[::-1]
        reversedTwo = num2[::-1]
        for idxOne in range(len(num1)):
            for idxTwo in range(len(num2)):
                res[idxOne+idxTwo] += int(reversedOne[idxOne]) * int(reversedTwo[idxTwo])
                res[idxOne+idxTwo+1] += res[idxOne+idxTwo] // 10
                res[idxOne+idxTwo] = res[idxOne+idxTwo] % 10
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        return "".join([str(x) for x in res[beg:]])
