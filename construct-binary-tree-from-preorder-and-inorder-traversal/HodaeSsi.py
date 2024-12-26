class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder == []:
            return None

        mid = preorder.pop(0)
        midIdx = inorder.index(mid)
        left = self.buildTree(preorder, inorder[:midIdx])
        right = self.buildTree(preorder, inorder[midIdx + 1:])

        return TreeNode(mid, left, right)

