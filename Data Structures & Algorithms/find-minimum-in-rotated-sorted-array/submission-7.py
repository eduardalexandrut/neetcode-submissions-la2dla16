class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mid = 0
        curr_min = float("inf")

        while l <= r:
            if nums[l] < nums[r]:
                curr_min =  min(curr_min, nums[l])
                break
            mid =(l + r) // 2
            curr_min = min(curr_min, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return curr_min