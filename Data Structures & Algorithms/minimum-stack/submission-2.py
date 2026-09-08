class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            currMin = self.stack[-1][1]
            self.stack.append((val, min(val, currMin)))
        

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()[0]
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]

        
