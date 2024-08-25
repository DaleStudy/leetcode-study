class Solution {
    private int i, p;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // Time complexity: O(n)
        // Space complexity: O(n)
        return builder(preorder, inorder, Integer.MIN_VALUE);
    }

    private TreeNode builder(int[] preorder, int[] inorder, int stop) {
        if (p >= preorder.length) return null;
        if (inorder[i] == stop) {
            i += 1;
            return null;
        }

        TreeNode node = new TreeNode(preorder[p]);
        p += 1;

        node.left = builder(preorder, inorder, node.val);
        node.right = builder(preorder, inorder, stop);
        return node;
    }
}
