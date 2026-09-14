class Solution:
    def isHappy(self, n: int) -> bool:

        seen_set = set()

        def dfs(num):
            print(num)
            if num in seen_set:
                return False
            if num == 1:
                return True
            res = 0
            for s in str(num):
                res += int(s)**2
            seen_set.add(num)
            return dfs(res)

        return dfs(n)
        