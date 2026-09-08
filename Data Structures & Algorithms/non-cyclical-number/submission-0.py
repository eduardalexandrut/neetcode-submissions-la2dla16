class Solution:
    def isHappy(self, n: int) -> bool:
        seen_set = set()

        while n != 1 and n not in seen_set:
            seen_set.add(n)
            n = sum(int(digit)**2 for digit in str(n))

        return n == 1