class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minVal = float("inf")
        tmpStack = []
        while self.stack:
            currVal = self.stack[-1]
            tmpStack.append(self.stack.pop())
            minVal = min(minVal, currVal)
        while tmpStack:
            self.stack.append(tmpStack.pop())
        return minVal
        
