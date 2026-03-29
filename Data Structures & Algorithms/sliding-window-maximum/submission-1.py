class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l= 0
        r = k - 1
        sol = []

        while r < len(nums):
            #find biggest in current substring
            sol.append(sorted(nums[l:r+1])[-1])
            l+=1
            r+=1
        
        return sol