class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        sol = 0

        while l < r:
            area = (r -l) * min(heights[l], heights[r])
            sol = max(sol, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return sol