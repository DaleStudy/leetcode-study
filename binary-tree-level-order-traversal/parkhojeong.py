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

        deq = deque()
        deq.append(root)

        output = []
        while deq:
            child = []
            level_nodes = []

            while deq:
                node = deq.popleft()
                level_nodes.append(node.val)
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)

            output.append(level_nodes)
            deq = deque(child)

        return output
