class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sorted_nums = sorted(set(nums))  # Remove duplicates and sort
        i = 0
        ans = 0
        
        while i < len(sorted_nums):
            j = i
            length = 1  # Start with length 1 for the current number
            
            while j + 1 < len(sorted_nums) and sorted_nums[j] + 1 == sorted_nums[j + 1]:
                length += 1
                j += 1
            
            ans = max(ans, length)
            i = j + 1  # Move to the next new number
        
        return ans
             
            