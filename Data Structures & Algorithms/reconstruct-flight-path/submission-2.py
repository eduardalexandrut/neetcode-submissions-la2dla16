class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        N = len(tickets)
        neighbors = collections.defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            neighbors[src].append(dst)

        res = []

        def dfs(src: str) -> None:
            while neighbors[src]:
                dst = neighbors[src].pop()
                dfs(dst)
            res.append(src)

        dfs("JFK")
        return res[::-1]