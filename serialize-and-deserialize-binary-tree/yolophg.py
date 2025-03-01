# Time Complexity:
# (1) serialize(): O(N) because traverse all nodes once.
# (2) deserialize(): O(N) because process each node once.
    
# Space Complexity:
# (1) serialize(): O(N) to store the serialized string.
# (2) deserialize(): O(N) for the queue and reconstructed tree.

class Codec:
    def serialize(self, root):
        # store the tree as a list of values (BFS style)
        ans = []
        if not root: 
            return "" 

        queue = [root]
        while queue:
            cur = queue.pop()
            if not cur:
                ans.append("n")  # use 'n' to represent null nodes
                continue
            ans.append(str(cur.val))  # add node value as string
            queue.append(cur.right)  # right first (for consistency in deserialization)
            queue.append(cur.left)  # then left
        
        return ",".join(ans)  # convert list to comma-separated string

    def deserialize(self, data):
        if not data: 
            return None
        
        data = deque(data.split(","))  # convert string back to list
        root = TreeNode(int(data.popleft()))  # first value is the root
        queue = [(root, 0)]  # track parent nodes and child positions
        
        while data:
            if not queue:
                return None  # should never happen unless input is corrupted
            
            cur = data.popleft()
            if cur == "n":
                val = None  # null node, no need to create a TreeNode
            else:
                val = TreeNode(int(cur))  # create a new TreeNode
            
            parent, cnt = queue.pop()  # get the parent and which child we’re setting
            if cnt == 0:
                parent.left = val  # assign left child
            else:
                parent.right = val  # assign right child
            
            cnt += 1  # move to the next child
            if cnt < 2:
                queue.append((parent, cnt))  # if parent still needs a right child, keep it in the queue
            if val:
                queue.append((val, 0))  # add new node to process its children later
        
        return root
