class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, ans = 0, len(height) - 1, 0
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                ans += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                ans  += maxR - height[r]
        return ans