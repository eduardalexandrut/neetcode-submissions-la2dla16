class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        sol = r

        while l <= r:
            mid = (l + r) // 2
            
            totTimeToEat = 0

            for i in range(0, len(piles)):
                totTimeToEat += (piles[i] + mid -1) // mid

            if totTimeToEat <= h:
                sol = mid
                r = mid - 1
            else:
                l = mid + 1

        return sol 