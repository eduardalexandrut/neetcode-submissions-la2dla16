class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_max = nums[0]
        lobal_max = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            
            if curr_max > lobal_max:
                lobal_max = curr_max

        return lobal_max