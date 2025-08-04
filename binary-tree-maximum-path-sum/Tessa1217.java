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

    // 최대 Path 누적 합
    int maxPathSumVal = Integer.MIN_VALUE;

    // 시간복잡도: O(n), 공간복잡도: O(h) h as height of tree
    public int maxPathSum(TreeNode root) {
        maxPathSumChecker(root);
        return maxPathSumVal;    
    }

    // 재귀
    private int maxPathSumChecker(TreeNode node) {

        if (node == null) {
            return 0;
        }

        int leftMax = Math.max(maxPathSumChecker(node.left), 0);
        int rightMax = Math.max(maxPathSumChecker(node.right), 0);

        maxPathSumVal = Math.max(node.val + leftMax + rightMax, maxPathSumVal);

        return node.val + Math.max(leftMax, rightMax);
    }
}

