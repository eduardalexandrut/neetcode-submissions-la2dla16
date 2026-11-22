class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        memo = {}
        target = total // 2

        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
                
            if i == len(nums) or curr_sum > target:
                return False

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            # Keep
            keep = dfs(i + 1, curr_sum + nums[i])
            # Skip
            skip = dfs(i + 1, curr_sum)

            memo[(i, curr_sum)] = skip or keep
            return memo[(i, curr_sum)]



        return dfs(0, 0)