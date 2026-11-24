class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i:list() for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visiting = set()
        visited = set()
        res = []

        def dfs(course):

            if course in visiting:
                return False

            if course in visited:
                return True

            #if preMap[course] == []:
            #    return True
            
            visiting.add(course)
            
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            preMap[course] = []
            visited.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res