class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(i, change):
            if change == 0:
                return 0

            if change < 0 or i >= len(coins):
                return 10_000_000
            
            if (i, change) in memo:
                return memo[(i, change)]

            # mantengo il caso attuale
            keep = 1 + dfs(i, change - coins[i])
            
            # skippo il caso attuale
            skip = dfs(i + 1, change)


            memo[(i, change)] = min(skip, keep)
            return memo[(i, change)]

        result = dfs(0, amount)
        if result != 10_000_000:
            return  result
        else:
            return -1
            