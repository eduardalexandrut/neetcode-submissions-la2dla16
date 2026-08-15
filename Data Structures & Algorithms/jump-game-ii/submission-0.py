class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0

        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])

            l = r + 1
            r = furthest
            jumps += 1

        return jumps