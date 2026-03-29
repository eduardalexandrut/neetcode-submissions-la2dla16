from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # stores indices
        l = r = 0

        while r < len(nums):
            # 1. Remove smaller values from the right of the deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # 2. Remove left index if it's out of window bounds
            if l > q[0]:
                q.popleft()

            # 3. If window is size k, add the max (front of q) to results
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
            
        return res