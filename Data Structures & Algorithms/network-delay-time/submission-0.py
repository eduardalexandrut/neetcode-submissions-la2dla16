class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = collections.defaultdict(list)
        for src, dst, weight in times:
            edges[src].append((dst, weight))
        minTime = 0

        visited = set()
        
        minHeap = [(0, k)]

        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            visited.add(node1)
            minTime = weight1

            for node2, weight2 in edges[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (weight1 + weight2, node2))

        return -1 if len(visited) != n else minTime