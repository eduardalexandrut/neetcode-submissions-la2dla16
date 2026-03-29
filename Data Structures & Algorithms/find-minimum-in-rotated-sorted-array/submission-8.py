class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        m = 0

        while l <= r:
            m = (l + r) //2
            if nums[m] > nums[r]:
                l += 1
            else:
                r -= 1

        return nums[m]