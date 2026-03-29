class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        Set = set()
        temp = None

        for i in range(len(nums)):
            if nums[i] in Set:
                return nums[i]
            else:
                Set.add(nums[i])

        return 0