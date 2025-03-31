# Time Complexity: O(n) -> visit each node exactly once.
# Space Complexity: O(n) -> in the worst case, the queue holds all nodes at the last level.

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # list to store level order traversal.
        ans = [] 
        
        # if the tree is empty, return an empty list.
        if root is None:
            return ans 
        
        # queue to process nodes level by level.
        q = deque([root]) 
        
        while q:
            # list to store values of nodes at the current level.
            t = [] 
            
            # process all nodes at this level.
            for _ in range(len(q)):  
                # pop the first node from the queue.
                node = q.popleft()  
                # add node's value to the list.
                t.append(node.val) 
                
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right) 
            
            # add current level values to the result list.
            ans.append(t) 
        
        return ans
