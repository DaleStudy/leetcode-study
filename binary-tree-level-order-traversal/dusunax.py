'''
# Leetcode 102. Binary Tree Level Order Traversal

do level order traversal

```
💡  why use BFS?:
BFS is the recommended approach, because it aligns with the problem's concept of processing the binary tree level by level and avoids issues related to recursion depth, making the solution both cleaner and more reliable.  

- DFS doesn't naturally support level-by-level traversal, so we need an extra variable like "dep" (depth).
- BFS is naturally designed for level traversal, making it a better fit for the problem.
- additionally, BFS can avoid potential stack overflow.
```

## A. BFS

### re-structuring the tree into a queue:
- use the queue for traverse the binary tree by level.

### level traversal:
- pop the leftmost node
- append the node's value to current level's array
- enqueue the left and right children to queue
- can only process nodes at the current level, because of level_size.

## B. DFS
- travase with a dep parameter => dp(node, dep)
- store the traversal result
'''
class Solution:
    '''
    A. BFS
    TC: O(n)
    SC: O(n)
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = [] # SC: O(n)
        queue = deque([root]) # SC: O(n)

        while queue: # TC: O(n)
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(level)

        return result

    '''
    B. DFS
    TC: O(n)
    SC: O(n)
    '''
    def levelOrderDP(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] # SC: O(n)

        def dp(node, dep):
            if node is None:
                return

            if len(result) <= dep:
                result.append([])

            result[dep].append(node.val)
            
            dp(node.left, dep + 1)
            dp(node.right, dep + 1)

        dp(root, 0) # TC: O(n) call stack

        return result
