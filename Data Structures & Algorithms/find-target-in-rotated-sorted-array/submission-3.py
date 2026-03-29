class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        while l < r:
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return -1