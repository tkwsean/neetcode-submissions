class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []
        def backtrack(openP, closeP):
            if(openP == closeP == n):
                res.append("".join(stack))
            if(openP < n):
                stack.append("(")
                backtrack(openP+1, closeP)
                stack.pop()
            if(closeP < openP):
                stack.append(")")
                backtrack(openP, closeP+1)
                stack.pop()
        backtrack(0, 0)
        return res 


















        # stack, res = [], []
        # def backtrack(openN, closedN):
        #     if openN == closedN == n:
        #         res.append("".join(stack))
        #     if openN < n:
        #         stack.append("(")
        #         backtrack(openN+1, closedN)
        #         stack.pop()
        #     if closedN < openN:
        #         stack.append(")")
        #         backtrack(openN, closedN+1)
        #         stack.pop()
        # backtrack(0, 0)
        # return res