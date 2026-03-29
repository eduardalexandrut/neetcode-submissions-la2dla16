class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        valToCount = dict()



        for n in nums:

            valToCount[n] = valToCount.get(n, 0) + 1



        return next((k for k,v in valToCount.items() if v>1), None)  