class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num-1 not in s:
                currentNum = num
                currentStreak = 1

                while currentNum + 1 in s:
                    currentNum += 1
                    currentStreak += 1
                longest = max(longest, currentStreak)

        return longest
            