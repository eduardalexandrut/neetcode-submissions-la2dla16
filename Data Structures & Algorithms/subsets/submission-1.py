class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        sol = []
        curr_sol = []

        def backtrack(index):
            if index >= len(nums):
                sol.append(curr_sol[:])
                return

            curr_sol.append(nums[index])
            backtrack(index + 1)

            curr_sol.pop()
            backtrack(index + 1)             

        backtrack(0)
        return sol
            