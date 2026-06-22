class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        max_reachable = 0

        for i in range(len(nums)):
            # If the current index is beyond the furthest we can reach, we are stuck
            if i > max_reachable:
                return False

            # Update the furthest index we can reach from here
            max_reachable = max(max_reachable, i + nums[i])

            if max_reachable >= target:
                return True

        return False