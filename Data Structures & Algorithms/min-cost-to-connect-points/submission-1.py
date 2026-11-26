class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        if n <= 1:
            return 0

        edges = []  # (dist, x, y)
        visited = set()
        sol = 0

        # Partiamo dal primo punto
        curr_x, curr_y = points[0]
        visited.add((curr_x, curr_y))

        while len(visited) < n:
            for x2, y2 in points:
                if (x2, y2) not in visited:
                    dist = abs(curr_x - x2) + abs(curr_y - y2)
                    heapq.heappush(edges, (dist, x2, y2))

            while edges:
                minDist, minX, minY = heapq.heappop(edges)
                if (minX, minY) not in visited:
                    visited.add((minX, minY))
                    sol += minDist
                    curr_x, curr_y = minX, minY
                    break

        return sol
