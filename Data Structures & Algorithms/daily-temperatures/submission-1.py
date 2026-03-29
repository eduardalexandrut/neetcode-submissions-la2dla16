class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i, val in enumerate(temperatures):
            count = 0
            for j in range(i +1 , len(temperatures)):
                if temperatures[j] > val:
                    count = j - i
                    break
            ans.append(count)
        return ans    