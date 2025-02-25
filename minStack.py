class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # minstack will hold the minimum values in the stack
        # we add a value if it is a new minimum otherwise we keep the same size
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
