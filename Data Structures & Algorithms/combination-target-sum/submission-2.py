class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol = []
        curr_sol = []
        def dfs(i, delta):
            if delta == 0:
                sol.append(list(curr_sol))
                return
            
            if delta < 0 or i == len(nums):
                return

            curr_sol.append(nums[i])
            dfs(i, delta - nums[i])
            curr_sol.pop()
            dfs(i + 1, delta)
            return

        dfs(0, target)
        return sol

