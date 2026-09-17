class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        memo = [0] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if memo[i] != 0:
                return memo[i]

            memo[i] = min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))

            return memo[i]


        return min(dfs(0), dfs(1))