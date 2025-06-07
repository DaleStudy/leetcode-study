from typing import List
from collections import defaultdict, deque

class Solution:
    """
        - Time Complexity: O(N + P), N = numCourses, P = len(prerequisites) 
        - Space Complexity: O(N + P)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topology Sort
        # BFS based, ingress count, visited
        ingress_cnt = [0] * numCourses
        dic = defaultdict(list)

        for dst, src in prerequisites:
            ingress_cnt[dst] += 1
            dic[src].append(dst)

        dq = deque([])            
        for dst in range(numCourses):
            if ingress_cnt[dst] == 0:
                dq.append(dst)

        visited_count = 0
        while dq:
            src = dq.popleft()
            visited_count += 1

            for dst in dic[src]:
                ingress_cnt[dst] -= 1
                if ingress_cnt[dst] == 0:
                    dq.append(dst)
        
        return visited_count == numCourses
    
tc = [
        (2, [[1,0]], True),
        (2, [[1,0],[0,1]], False)
]

sol = Solution()
for i, (n, p, e) in enumerate(tc, 1):
    r = sol.canFinish(n, p)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
