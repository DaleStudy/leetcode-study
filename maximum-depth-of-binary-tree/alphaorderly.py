# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Time Complexity: O(N)
Space Complexity: O(N) - Recursive stack space

### Recursive Solution ###

1. If the root is None, return 0
2. Return the maximum of the depth of the left and right subtrees + 1
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

"""
Time Complexity: O(N)
Space Complexity: O(N) - Stack space

### Iterative Solution ( DFS ) ###

1. If the root is None, return 0
2. Use a stack to store the nodes and the level of the nodes
3. Pop the nodes from the stack and update the maximum depth
4. If the node has a left child, add the left child and the level + 1 to the stack
5. If the node has a right child, add the right child and the level + 1 to the stack
6. Return the maximum depth
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        s = [(root, 1)]
        ans = 1

        while s:
            node, level = s.pop()
            ans = max(ans, level)

            if node.left:
                s.append((node.left, level + 1))

            if node.right:
                s.append((node.right, level + 1))

        return ans

"""
Time Complexity: O(N)
Space Complexity: O(N) - Queue space

### Iterative Solution ( BFS ) ###

1. If the root is None, return 0
2. Use a queue to store the nodes and the level of the nodes
3. Pop the nodes from the queue and update the maximum depth
4. If the node has a left child, add the left child and the level + 1 to the queue
5. If the node has a right child, add the right child and the level + 1 to the queue
6. Return the maximum depth
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        ans = 1

        while q:
            node, level = q.popleft()
            ans = max(ans, level)

            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

        return ans

"""
Time Complexity: O(N)
Space Complexity: O(N) - Queue space

### Iterative Solution ( Level Order Traversal ) ###

1. If the root is None, return 0
2. Use a queue to store the nodes
3. Pop the nodes from the queue and update the maximum depth
4. If the node has a left child, add the left child to the queue
5. If the node has a right child, add the right child to the queue
6. Return the maximum depth
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        level = 0

        while q:
            level += 1
            N = len(q)
            for _ in range(N):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
        
        return level
