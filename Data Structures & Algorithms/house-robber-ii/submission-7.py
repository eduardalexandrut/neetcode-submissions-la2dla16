class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        memo = {}

        def dfs(i, startedFromFirst):

            if (startedFromFirst and i >= len(nums) - 1) or (not startedFromFirst and i >= len(nums)):
                return 0

            if (i, startedFromFirst) in memo:
                return memo[(i, startedFromFirst)]

            memo[(i, startedFromFirst)] = max(dfs(i + 1, startedFromFirst), nums[i] + dfs(i + 2, startedFromFirst))

            return memo[(i, startedFromFirst)]

        return max(dfs(0, True), dfs(1, False))