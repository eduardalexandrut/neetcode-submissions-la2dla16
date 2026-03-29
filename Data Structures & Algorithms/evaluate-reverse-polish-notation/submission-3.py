class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem == '+':
                prev = stack.pop()
                res = stack.pop() + prev
                stack.append(res)
            elif elem == '*':
                prev = stack.pop()
                res = stack.pop() * prev
                stack.append(res)
            elif elem == '-':
                prev = stack.pop()
                res = stack.pop() - prev
                stack.append(res)
            elif elem == '/':
                prev = stack.pop()
                res = int(float(stack.pop()) / prev)
                stack.append(res)
            else:
                stack.append(int(elem))
        return round(stack[-1])