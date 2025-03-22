/*
# Time Complexity: O(n)
# Space Complexity: O(n)
  - 재귀 호출 파라미터 O(n) 사이즈 공간 필요
*/

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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        return dfs(root, subRoot);
    }

    private boolean dfs(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) return true;
        if (root == null || subRoot == null) return false;

        if (root.val == subRoot.val) {
            if (compareTrees(root, subRoot)) return true;
        }

        if (dfs(root.left, subRoot)) return true;
        if (dfs(root.right, subRoot)) return true;

        return false;
    }

    private boolean compareTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return true;
        if (root1 == null || root2 == null) return false;

        if (root1.val != root2.val) return false;

        return compareTrees(root1.left, root2.left) && compareTrees(root1.right, root2.right);
    }
}
