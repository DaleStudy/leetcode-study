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
    /*
    time complexity: O(n)
    space complexity: O(h)
     */
    int maxDepth = 0;

    public int maxDepth(TreeNode root) {
        depthChk(root, 0);
        return maxDepth;
    }

    public void depthChk(TreeNode node, int depth) {
        if (node == null) {
            maxDepth = Math.max(depth, maxDepth);
            return;
        }

        // 트리의 좌우 탐색
        depthChk(node.left, depth + 1);
        depthChk(node.right, depth + 1);
    }
}
