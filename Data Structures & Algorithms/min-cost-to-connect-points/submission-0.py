class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        numNodes = len(points)
        distHeap = [(0,0)]
        cost = 0
        visited = set()

        while len(visited) < numNodes:
            # Get current closest point
            currDist, currNode = heapq.heappop(distHeap)

            if currNode in visited:
                continue

            visited.add(currNode)

            cost += currDist

            ux, uy = points[currNode]
            for v in range(numNodes):
                if v not in visited:
                    vx, vy = points[v]
                    dist = abs(ux - vx) + abs(uy - vy)
                    heapq.heappush(distHeap, (dist, v))


        return cost


