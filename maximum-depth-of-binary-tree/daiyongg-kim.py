class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            print(len(queue))
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


#        if not root:
#            return 0
        
#        left_depth = self.maxDepth(root.left)
#        right_depth = self.maxDepth(root.right)

#        return max(left_depth, right_depth) + 1
