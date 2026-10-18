class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        sol = []
        def dfs(i, curr_sol):
            if i == len(nums):
                sol.append(list(curr_sol))
                return
            curr_sol.append(nums[i])
            dfs(i + 1, curr_sol)
            curr_sol.pop()
            dfs(i + 1, curr_sol)
            return

        dfs(0, [])
        return sol

