class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        curr_sol = []


        def dfs(i):
            if i >= len(nums):
                sol.append(list(curr_sol))
                return
            
            curr_sol.append(nums[i])
            dfs(i + 1)
            curr_sol.pop()
            dfs(i + 1)
            return

        dfs(0)
        return sol