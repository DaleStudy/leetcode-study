class Solution:
    def buildTree(self, preorder, inorder):
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            in_root_idx = inorder_index_map[root_val]
            left_size = in_root_idx - in_left
            root.left = build(pre_left + 1, pre_left + left_size, in_left, in_root_idx - 1)
            root.right = build(pre_left + left_size + 1, pre_right, in_root_idx + 1, in_right)
            return root
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
