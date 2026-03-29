class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        sol = 0

        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            area = base * height
            sol = max(sol, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return sol

        