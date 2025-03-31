# Time Complexity: O(V + E) - visit each course once and process all edges
# Space Complexity: O(V + E) - storing the graph + recursion stack (worst case)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build the adjacency list (prereq map)
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # tracks courses currently being checked (for cycle detection)
        visited = set()  

        def dfs(crs):
            # found a cycle
            if crs in visited:  
                return False
            # no more prereqs left
            if preMap[crs] == []: 
                return True
            
            # mark as visiting
            visited.add(crs)  
            
            # check all prereqs for this course
            for pre in preMap[crs]:
                if not dfs(pre):
                    # cycle detected, return False
                    return False  
            
            # done checking, remove from visited
            visited.remove(crs)  
            # mark as completed
            preMap[crs] = []  
            return True

        # run dfs on every course
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True  
