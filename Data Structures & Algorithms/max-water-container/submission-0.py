class Solution:
    def maxArea(self, heights: List[int]) -> int:
        stack = [0]
        l = 0
        r = len(heights) - 1

        while l < r:
            smallest = min(heights[l], heights[r])
            base = r - l
            area = base * smallest
            if stack[0] < area:
                stack.pop()
                stack.append(area)
            if smallest == heights[l]:
                l+=1
            else:
                r-=1
        return stack[0]
        