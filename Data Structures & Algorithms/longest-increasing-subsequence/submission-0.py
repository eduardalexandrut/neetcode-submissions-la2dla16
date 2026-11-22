class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        s = []

        def dfs(i, prev_idx):
            if i == len(nums):
                return 0

            if (i, prev_idx) in memo:
                return memo[(i, prev_idx)]

            skip = dfs((i+1), prev_idx)

            take = 0
            if prev_idx == -1 or nums[prev_idx] < nums[i]:
                take = 1 + dfs(i + 1, i)

            memo[(i, prev_idx)] = max(skip, take)
            return memo[(i, prev_idx)]
            

        return dfs(0, -1)

        