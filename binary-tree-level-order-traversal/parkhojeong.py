# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        deq = deque([root])

        output = []
        while deq:
            nodes = []

            for _ in range(len(deq)):
                node = deq.popleft()
                nodes.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)

            output.append(nodes)

        return output
