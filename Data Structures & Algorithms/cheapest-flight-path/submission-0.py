class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0

        for _ in range(k + 1):
            temp = costs.copy()
            for (u, v, price) in flights:

                if costs[u] != float("inf") and costs[u] + price < temp[v]:
                    temp[v] = costs[u] + price

            costs = temp

        if costs[dst] != float("inf"):
            return costs[dst]

        return -1