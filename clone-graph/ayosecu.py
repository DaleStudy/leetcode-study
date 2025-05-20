from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """
        - Time Complexity: O(N + E)
            - N = The number of nodes
            - E = The number of neighbors
        - Space Complexity: O(N + E)
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        dq = deque([node])
        dic = {}
        dic[node] = Node(node.val)

        while dq:
            pop_node = dq.popleft()        

            for n in pop_node.neighbors:
                if n not in dic:
                    dq.append(n)
                    dic[n] = Node(n.val)
                dic[pop_node].neighbors.append(dic[n])

        return dic[node]             


### TEST CASES ###
def build_graph(adj_list):
    if not adj_list:
        return None

    nodes = {}
    for i in range(1, len(adj_list) + 1):
        nodes[i] = Node(i)

    for i, neighbors in enumerate(adj_list, 1):
        nodes[i].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]


def print_graph(node):
    if not node:
        print("None")
        return
    
    visited = set()
    q = deque([node])
    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        print(f"Node {curr.val}: {[n.val for n in curr.neighbors]}")
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                q.append(neighbor)

tc = [
        [[2,4],[1,3],[2,4],[1,3]],
        [[]],
        []
]

sol = Solution()
for i, adj_list in enumerate(tc, 1):
    original = build_graph(adj_list)
    print(f"===== TC {i} =====")
    print("Original Graph:")
    print_graph(original)

    cloned = sol.cloneGraph(original)

    print("\nCloned Graph:")
    print_graph(cloned)
