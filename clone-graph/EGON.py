from typing import Optional, TypeVar
from unittest import TestCase, main


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        return self.solve(node)

    """
    Runtime: 42 ms (Beats 45.48%)
    Time Complexity: O(n)

    Memory: 17.04 (Beats 8.15%)
    Space Complexity: O(n), upper bound
    """
    def solve(self, node: Optional[Node]) -> Optional[Node]:
        clone_dict = {}
        stack = [node]
        visited = set()
        while stack:
            curr_node = stack.pop()
            visited.add(curr_node.val)
            if curr_node.val not in clone_dict:
                clone_dict[curr_node.val] = Node(val=curr_node.val)

            for neighbor in curr_node.neighbors:
                if neighbor.val not in clone_dict:
                    clone_dict[neighbor.val] = Node(val=neighbor.val)

                if neighbor.val not in visited:
                    clone_dict[curr_node.val].neighbors.append(clone_dict[neighbor.val])
                    clone_dict[neighbor.val].neighbors.append(clone_dict[curr_node.val])
                    stack.append(neighbor)

        return clone_dict[node.val]


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        node_dict = {1: Node(1), 2: Node(2), 3: Node(3), 4: Node(4)}
        node_dict[1].neighbors = [node_dict[2], node_dict[4]]
        node_dict[2].neighbors = [node_dict[1], node_dict[3]]
        node_dict[3].neighbors = [node_dict[2], node_dict[4]]
        node_dict[4].neighbors = [node_dict[1], node_dict[3]]

        Solution.cloneGraph(Solution(), node_dict[1])
        self.assertTrue("RUN")


if __name__ == '__main__':
    main()
