class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        curr_sol = []

        def dfs(i):
            if i >= len(nums):
                sol.append(curr_sol.copy())
                return


            curr_sol.append(nums[i])
            dfs(i + 1)

            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            i = j

            curr_sol.pop()
            dfs(i)
        
        dfs(0)
        return sol
        