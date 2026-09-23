class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.insert(0, (val, val))
        else:
            currMinVal = self.stack[0][1]
            self.stack.insert(0, (val,min(val, currMinVal)))

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]
    

        
