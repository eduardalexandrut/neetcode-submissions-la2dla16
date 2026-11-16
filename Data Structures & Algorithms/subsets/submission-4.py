class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        sol = []
        curr_sol = []

        def dfs(i):

            # base case
            if i >= len(nums):
                sol.append(list(curr_sol))
                cur_sol = []
                return
            
            # try with curr
            curr_sol.append(nums[i])
            dfs(i + 1)

            #try without curr(next)
            curr_sol.pop()
            dfs(i + 1)
        
        dfs(0)
        return sol
