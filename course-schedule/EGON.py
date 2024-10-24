from collections import deque
from typing import List
from unittest import TestCase, main


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.solve_topological_sort(numCourses, prerequisites)

    """
    Runtime: 1 ms (Beats 100.00%)
    Time Complexity: o(c + p)
        - graph 및 rank 갱신에 prerequisites의 길이 p만큼 조회하는데 O(p)
        - queue의 초기 노드 삽입에 numCourses만큼 조회하는데 O(c)
        - queue에서 위상 정렬로 탐색하는데 모든 노드와 간선을 조회하는데 O(c + p)
        > O(p) + O(c) + O(c + p) ~= o(c + p)

    Memory: 17.85 MB (Beats 99.94%)
    Space Complexity: O(c)
        - graph 변수 사용에 O(c + p)
        - rank 변수 사용에 O(c)
        - queue 변수 사용에서 최대 크기는 graph의 크기와 같으므로 O(c)
        > O(c + p) + O(c) + O(c) ~= O(c + p)
    """
    def solve_topological_sort(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        rank = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            rank[u] += 1

        queue = deque()
        for i in range(numCourses):
            if rank[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                rank[neighbor] -= 1
                if rank[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        numCourses = 5
        prerequisites = [[1,4],[2,4],[3,1],[3,2]]
        output = True
        self.assertEqual(Solution.canFinish(Solution(), numCourses, prerequisites), output)


if __name__ == '__main__':
    main()
