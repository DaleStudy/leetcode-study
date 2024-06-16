class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        return_list = []

        while queue:
            level_size = len(queue)
            current_level = []

            for n in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            return_list.append(current_level)

        return return_list

        ## TC: O(n), SC: O(n)
