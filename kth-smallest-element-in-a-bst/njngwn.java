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
    int cnt = 0;
    int result = 0;

    public int kthSmallest(TreeNode root, int k) {
        cnt = k;
        traverseInOrder(root);
        return result;
    }

    public void traverseInOrder (TreeNode node) {
        if (node == null) return;

        if (node.left != null) traverseInOrder(node.left);
        cnt--;
        if (cnt == 0) {
            result = node.val;
            return;
        }
        if (node.right != null) traverseInOrder(node.right);
    }
}
