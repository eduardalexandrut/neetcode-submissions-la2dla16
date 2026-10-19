class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        curr_sol = []

        def dfs():
            if  len(curr_sol) == len(nums):
                sol.append(list(curr_sol))
                return
            for num in nums:
                if num not in curr_sol:
                    curr_sol.append(num)
                    dfs()
                    curr_sol.pop()
            return

        dfs()
        return sol