# Time Complexity: O(N + E) - visit each node once and for each node, we iterate through its neighbors O(E).
# Space Complexity: O(N) - store a copy of each node in the hashmap O(N).

class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
    
        # dictionary to keep track of cloned nodes (original -> clone)
        mp = {} 

        def clone(node):
            if node in mp:
                # if the node has already been cloned, return the copy
                return mp[node]  

            # create a new node with the same value
            cpy = Node(node.val)  
            # store it in the map so don't clone it again
            mp[node] = cpy  

            # clone all neighbors and add them to the new node's neighbors list
            for n in node.neighbors:
                cpy.neighbors.append(clone(n))

            return cpy

        return clone(node)
