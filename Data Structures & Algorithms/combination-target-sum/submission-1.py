class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        curr_sol = []

        def backtracking(i, curr_sum):
            if curr_sum == target:
                sol.append(curr_sol[:])
                return

            if i >= len(nums) or curr_sum > target:
                return

            curr_sol.append(nums[i])
            backtracking(i, curr_sum + nums[i])
            
            curr_sol.pop()
            backtracking(i + 1, curr_sum)

        backtracking(0, 0)
        return sol 
            
