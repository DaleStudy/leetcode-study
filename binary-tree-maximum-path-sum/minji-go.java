/**
 * <a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/">week11-5. binary-tree-maximum-path-sum</a>
 * <li>Description: Given the root of a binary tree, return the maximum path sum of any non-empty path</li>
 * <li>Topics: Dynamic Programming, Tree, Depth-First Search, Binary Tree</li>
 * <li>Time Complexity: O(N), Runtime 0ms   </li>
 * <li>Space Complexity: O(H), Memory 44.1MB</li>
 */
class Solution {
    public int maxPathSum(TreeNode root) {
        dfs(root);
        return max;
    }

    int max = Integer.MIN_VALUE;
    public int dfs(TreeNode head) {
        if (head == null) return 0;

        int left = Math.max(0, dfs(head.left));
        int right = Math.max(0, dfs(head.right));

        max = Math.max(max, head.val + left + right);

        return head.val + Math.max(left, right);
    }

}
