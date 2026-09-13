class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t == "+":
                s.append(s.pop() + s.pop())
            elif t == "*":
                s.append(s.pop() * s.pop())
            elif t == "-":
                r = s.pop()
                l = s.pop()
                s.append(l - r)
            elif t == "/":
                r = s.pop()
                l = s.pop()
                s.append(int(float(l / r)))
            else:
                s.append(int(t))

        return s.pop()