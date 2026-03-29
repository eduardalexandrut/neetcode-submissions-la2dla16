class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #Get the smallest value by checking the last value in minStack and the ne value to be added
        smallest = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(smallest)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
