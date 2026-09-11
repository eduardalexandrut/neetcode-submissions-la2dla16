class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()
        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                remaining_time = 1 + heapq.heappop(max_heap)
                if remaining_time:
                    q.append([remaining_time, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time