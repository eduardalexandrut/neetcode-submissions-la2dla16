class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = []

        for n in nums:
            heapq.heappush(s, n)
            while len(s) > k:
                heapq.heappop(s)

        return heapq.heappop(s)