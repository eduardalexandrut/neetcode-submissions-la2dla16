class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reachable = 0
        target = len(nums) - 1

        for i in range(len(nums)):
            if i > max_reachable:
                return False

            max_reachable = max(max_reachable, i + nums[i])

            if max_reachable >= target:
                return True

        return False