class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        best = nums[0]

        for curr in nums[1:]:
            prev_max = cur_max
            cur_max = max(curr, curr * prev_max, curr * cur_min)
            cur_min = min(curr, curr * prev_max, curr * cur_min)
            best = max(best, cur_max)

        return best