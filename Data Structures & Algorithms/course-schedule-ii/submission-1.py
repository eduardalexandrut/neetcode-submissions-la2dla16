class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:list() for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()  # Tracks nodes in the current DFS path (for cycle detection)
        visited = set()   # Tracks nodes fully processed and added to 'res'
        res = []

        def dfs(course):
            if course in visiting:
                # Cycle detected
                return False

            if course in visited:
                return True

            visiting.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            preMap[course] = []
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res