class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        return True if fast == 1 else False


    def sumOfSquares(self, n):
        res = 0
        for s in str(n):
            res += int(s)**2

        return res