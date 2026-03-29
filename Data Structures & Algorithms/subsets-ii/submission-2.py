class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        curr_sol = []

        def back(i):
            if i >= len(nums):
                sol.append(curr_sol[:])
                return

            curr_sol.append(nums[i])
            back(i + 1)

            curr_sol.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            back(i+1)

        back(0)
        return sol
        