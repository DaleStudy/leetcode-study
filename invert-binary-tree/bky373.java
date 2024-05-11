/**
 * - 문제: https://leetcode.com/problems/linked-list-cycle/
 * - TC: O(N)
 * - SC: O(N)
 */
public class Solution_226 {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode tmp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(tmp);
        return root;
    }
}
