class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            heap.append((distance,point))
        
        heapq.heapify(heap)
        return [point for _, point in heapq.nsmallest(k,heap)]
