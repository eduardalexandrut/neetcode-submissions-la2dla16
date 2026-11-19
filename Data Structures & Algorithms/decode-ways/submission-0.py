class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}

        def dfs(i):
            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]

            # Option 1
            ways = dfs(i + 1)

            # Option 2
            if i + 2 <= len(s) and "10" <= s[i:i+2] <= "26":
                ways += dfs(i + 2)

            memo[i] = ways
            return memo[i]

        return dfs(0)