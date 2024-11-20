// TC: O(n)
// need to check all nodes in the worst case
// SC: O(n)
// recursion requires O(n) SC in the worst case
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;

        if (sameCheck(root, subRoot)) return true;

        return isSubtree(root.left, subRoot) ||
                isSubtree(root.right, subRoot);
    }

    private boolean sameCheck(TreeNode root, TreeNode subRoot) {
        if (root == null || subRoot == null) {
            return root == null && subRoot == null;
        }

        if (root.val != subRoot.val) return false;

        return sameCheck(root.left, subRoot.left) &&
                sameCheck(root.right, subRoot.right);
    }
}
