class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = dict()

        for val in nums:
            if val in m:
                return True
            m[val] = val

        return False
        