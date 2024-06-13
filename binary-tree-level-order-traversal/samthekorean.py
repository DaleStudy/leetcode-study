# TC : O(n)
# SC : O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            level = []
            qLen = len(q)

            # traverse nodes in each level and append left and right subtree if node is None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # append the subtrees of q for the next level in advance
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
