class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # compare the bottom element with the top element in stack
        # if we have top element > bottom element, return the difference in indexes 
        stack = []
        currIndex = 0
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                value, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i], i))
        return res