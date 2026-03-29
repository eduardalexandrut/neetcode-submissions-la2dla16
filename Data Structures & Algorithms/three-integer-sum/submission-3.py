class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for index, val in enumerate(nums):
            if val > 0:
                break
            #check if the current number and the previous are the same(dulicate), and if so skip
            if index > 0 and val == nums[index - 1]:
                continue

            l, r = index + 1, len(nums) - 1

            while l < r:
                threeSum = val + nums[l] + nums[r]

                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    ans.append([val, nums[l], nums[r]])
                    l += 1
                    #Keep shifting thhe left pointer so that we exclude duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans