class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # filter false cases by definition of tree
        if n - 1 != len(edges):
            return False

        nodes = set()

        for i, edge in enumerate(edges):
            nodes.add(edge[0])
            nodes.add(edge[1])

            if i + 1 > len(nodes) - 1:
                return False

        return True

        ## TC: O(num(edges)), SC: P(num(nodes))
