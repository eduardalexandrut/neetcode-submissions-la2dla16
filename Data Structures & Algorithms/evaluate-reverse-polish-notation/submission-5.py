class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == "+":
                stack.append(stack.pop() + stack.pop())
            elif s == "-":
                l = stack.pop()
                r = stack.pop()
                stack.append(r - l)
            elif s == "*":
                stack.append(stack.pop() * stack.pop())
            elif s == "/":
                l = stack.pop()
                r = stack.pop()
                stack.append(int(float(r) / l))
            else:
                stack.append(int(s))

        return stack.pop()
