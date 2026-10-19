class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        curr_sol = []

        def dfs(i):
            if i >= len(nums):
                sol.append(list(curr_sol))
                return

            curr_sol.append(nums[i])
            dfs(i + 1)
            curr_sol.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
            return

        dfs(0)
        return sol
        