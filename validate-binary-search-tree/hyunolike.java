/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValid(root, null, null);     
    }

    private boolean isValid(TreeNode node, Integer min, Integer max) {
        if (node == null) {
            return true;
        }

        if (min != null && node.val <= min) return false;
        if (max != null && node.val >= max) return false;

        return isValid(node.left, min, node.val) && isValid(node.right, node.val, max);
    }
}
