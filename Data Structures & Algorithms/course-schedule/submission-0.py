class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #hashmap = {0: []}
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for i, prereq in prerequisites:
            preMap[i].append(prereq)

        print(preMap)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            
            visited.add(course)
            for nei in preMap[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
            
            


