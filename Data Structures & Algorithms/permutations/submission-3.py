class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        curr_sol = []

        def dfs():
            
            if len(curr_sol) == len(nums):
                sol.append(curr_sol.copy())
                return

            for n in nums:
                if n not in curr_sol:
                    curr_sol.append(n)
                    dfs()
                    curr_sol.pop()

        dfs()
        return sol 