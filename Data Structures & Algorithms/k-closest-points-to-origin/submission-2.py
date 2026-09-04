class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sol = []
       
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt((x)**2 + (y)**2)
            sol.append((dist, x, y))

        heapq.heapify(sol)

        a = []
        while k > 0:
            curr = heapq.heappop(sol)
            a.append((curr[1], curr[2]))
            k -= 1

        return a