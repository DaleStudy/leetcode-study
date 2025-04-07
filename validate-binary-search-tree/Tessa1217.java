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
/**
 이진 트리의 root가 주어졌을 때 유효한 이진 탐색 트리인지 검증하세요.
 */
class Solution {

    /** 시간복잡도 O(n) */
    public boolean isValidBST(TreeNode root) {
        return isValidRange(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean isValidRange(TreeNode root, long min, long max) {
        if (root == null) {
            return true;
        }
        if (root.val <= min || root.val >= max) {
            return false;
        }
        return isValidRange(root.left, min, root.val) && isValidRange(root.right, root.val, max);
    }
}

