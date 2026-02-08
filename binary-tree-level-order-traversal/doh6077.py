from collections import deque
# 102. Binary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. Edge Case: Empty Tree
        if not root:
            return [] 
        
        result = [] 
        queue = deque([root])
        
        while queue:
            # 2. Capture the number of nodes at the current level
            level_size = len(queue)
            current_level_nodes = []
            
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level_nodes.append(current_node.val)
                
                # 3. Add children to the queue for the NEXT level
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right: 
                    queue.append(current_node.right)
            
            # Add the finished level to our result
            result.append(current_level_nodes)
            
        return result