"""TC: O(node + edge), SC: O(node + edge)

유명한 위상 정렬 알고리즘이므로 설명은 생략한다.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 위상 정렬.

        # init
        adj_list = [[] for _ in range(numCourses)]  # SC: O(edge)
        in_deg = [0] * numCourses  # SC: O(node)

        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])
            in_deg[edge[1]] += 1

        node_to_search = [i for i, v in enumerate(in_deg) if v == 0]  # TC: O(node)
        sorted_list = []

        # process
        while node_to_search:
            cur = node_to_search.pop()  # TC: 최악의 경우 총 O(node)만큼 실행
            sorted_list.append(cur)
            for node in adj_list[cur]:
                in_deg[node] -= 1  # TC: 최악의 경우 총 O(edge)만큼 실행
                if in_deg[node] == 0:
                    node_to_search.append(node)

        return len(sorted_list) == numCourses
