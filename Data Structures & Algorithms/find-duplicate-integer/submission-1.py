#Good solution but space complexity: O(n)
#def findDuplicate(self, nums: List[int]) -> int:
#        Set = set()
#
#       for i in range(len(nums)):
#            if nums[i] in Set:
#                return nums[i]
#            else:
#                Set.add(nums[i])
#
#        return 0


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        #Use Floyd's algorithm to find a cycle.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        #Find the duplicate
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
