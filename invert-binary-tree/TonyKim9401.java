// TC: O(n)
// -> visit all nodes to invert
// SC: O(n)
// -> create all nodes again to exchange
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        invertTree(root.left);
        invertTree(root.right);
        TreeNode left = root.left;
        TreeNode right = root.right;
        root.left = right;
        root.right = left;
        return root;
    }
}
