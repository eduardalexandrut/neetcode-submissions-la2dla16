class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def backtrack(start, current, total):
            #If the total of this path is the same as the target, add it to res
            if total == target:
                res.append(current[:])
                return

            #If the total of this path exceeds the target, stop exploring this path
            if total > target:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, total + nums[i])
                current.pop()

        res = []
        backtrack(0, [], 0)
        return res
        