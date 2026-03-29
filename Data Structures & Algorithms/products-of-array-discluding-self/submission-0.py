class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            product = 0
            left = nums[:i]
            right = nums[i+1:]

            left_p = 1
            for val in left:
                left_p*=val

            right_p = 1
            for val in right:
                right_p*=val
            product = left_p * right_p
            ans.append(product)
        return ans
