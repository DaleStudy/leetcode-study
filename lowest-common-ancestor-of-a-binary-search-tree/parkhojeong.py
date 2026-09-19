# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def search(node: TreeNode, target: int):
            stack = [node]
            arr = []
            while stack:
                node = stack.pop()
                arr.append(node)
                if node.val > target:
                    stack.append(node.left)
                elif node.val < target:
                    stack.append(node.right)

            return arr

        arr1 = set(search(root, p.val))
        arr2 = search(root, q.val)

        for node in arr2[::-1]:
            if node in arr1:
                return node
