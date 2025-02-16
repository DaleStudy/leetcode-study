'''
# 226. Invert Binary Tree

switch left and right child of each node

## TC: O(N)

visit each node once

## SC: O(h)

h is height of tree

- best case: O(logN), balanced tree
- worst case: O(N), skewed tree
'''
class Solution:
    '''
    DFS
    '''
    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    '''
    BFS
    - 직관적인 stack 풀이
    '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue
            
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)

        return root

    '''
    - 참고용 deque 풀이
    '''
    def invertTreeDeque(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([root])

        while dq:
            node = dq.popleft()
            if not node:
                continue
            
            node.left, node.right = node.right, node.left
            dq.append(node.left)
            dq.append(node.right)

        return root
