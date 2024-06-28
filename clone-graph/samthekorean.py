# TC : O(n)
# SC : O(n)
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        # Dictionary to store cloned nodes
        cloned_nodes = {}
        # BFS queue starting with the original node
        queue = deque([node])

        # Clone the original node
        cloned_node = Node(node.val)
        cloned_nodes[node] = cloned_node

        while queue:
            current_node = queue.popleft()

            # Iterate through neighbors of the current node
            for neighbor in current_node.neighbors:
                if neighbor not in cloned_nodes:
                    # Clone the neighbor and add it to the queue
                    cloned_neighbor = Node(neighbor.val)
                    cloned_nodes[neighbor] = cloned_neighbor
                    queue.append(neighbor)

                # Add the cloned neighbor to the cloned current node's neighbors list
                cloned_nodes[current_node].neighbors.append(cloned_nodes[neighbor])

        return cloned_node
