class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(sol, start):
            res.append(sol[:])

            for i in range(start, len(nums)):
                sol.append(nums[i])
                backtrack(sol, i + 1)
                sol.pop()

        backtrack([],0)
        return res