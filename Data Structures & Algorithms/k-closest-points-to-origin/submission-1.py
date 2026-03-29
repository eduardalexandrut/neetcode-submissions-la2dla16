class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
    
        for p in points:
            x = p[0]
            y = p[1]
            dist = math.sqrt((x)**2 + (y)**2)
            distances.append((dist, [x, y]))

        heapq.heapify(distances)
        sol = []
        while k > 0:
            dist, coords = heapq.heappop(distances)
            sol.append(coords)
            k-=1
        return sol