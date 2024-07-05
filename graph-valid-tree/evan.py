from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If the number of edges is not equal to n-1, it can't be a tree
        if len(edges) != n - 1:
            return False

        # Initialize node_list array where each node is its own parent
        node_list = list(range(n))

        # Find root function with path compression
        def find_root(node):
            if node_list[node] != node:
                node_list[node] = find_root(node_list[node])

            return node_list[node]

        def union_and_check_cycle(node1, node2):
            root1 = find_root(node1)
            root2 = find_root(node2)

            if root1 != root2:
                node_list[root2] = root1
                return True
            else:
                return False

        for node1, node2 in edges:
            if not union_and_check_cycle(node1, node2):
                return False

        return True


# Example usage:
solution = Solution()
print(solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # Output: True
print(solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # Output: False
