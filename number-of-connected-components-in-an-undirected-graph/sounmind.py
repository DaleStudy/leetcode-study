from typing import List


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # Initialize each node to be its own parent
        vertex_list = list(range(n))

        # Helper function to find the root of a node
        def find(node):
            while vertex_list[node] != node:
                node = vertex_list[node]
            return node

        # Iterate through each edge and perform union
        for edge in edges:
            root1 = find(edge[0])
            root2 = find(edge[1])

            # If roots are different, union the components
            if root1 != root2:
                for i in range(n):
                    if vertex_list[i] == root1:
                        vertex_list[i] = root2

        # Find all unique roots to count the number of connected components
        unique_roots = set(find(i) for i in range(n))
        return len(unique_roots)


# Test Cases
solution = Solution()

print(solution.count_components(4, [[0, 1], [2, 3], [3, 1]]))  # Output: 1
print(solution.count_components(5, [[0, 1], [1, 2], [3, 4]]))  # Output: 2
print(solution.count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # Output: 1
print(solution.count_components(3, [[0, 1], [1, 2], [2, 0]]))  # Output: 1
print(solution.count_components(4, []))  # Output: 4
print(
    solution.count_components(7, [[0, 1], [1, 2], [3, 4], [4, 5], [5, 6]])
)  # Output: 2
