class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        atlanticSet = set()
        pacificSet = set()

        aQ = deque([])
        pQ = deque([])

        for r in range(ROWS):
            pQ.append((r, 0))
            aQ.append((r, COLS - 1))

        for c in range(COLS):
            pQ.append((0, c))
            aQ.append((ROWS - 1, c))

        def bfs(starts):
            reachable = set()
            reachable.update(starts)

            while starts:
                rr, cc = starts.popleft()

                for dr, dc in directions:
                    nr = rr + dr
                    nc = cc + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in reachable:
                        if heights[nr][nc] >= heights[rr][cc]:
                            starts.append((nr, nc))
                            reachable.add((nr, nc))
            return reachable

        pacificSet = bfs(pQ)
        atlanticSet = bfs(aQ)

        return [list(cell) for cell in pacificSet.intersection(atlanticSet)]






