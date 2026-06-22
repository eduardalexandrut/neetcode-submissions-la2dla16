class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            # Decide whether to add the current number to the existing streak(current_max + nums[i]),
            # or throw away the past and start fresh with nums[i]
            current_max = max(nums[i], current_max + nums[i])

            if current_max > global_max:
                global_max = current_max

        return global_max
            
