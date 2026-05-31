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
    int depth = 0;
    int answer = 0;
    public int kthSmallest(TreeNode root, int k) {
        inOrder(root, k);
        return answer;
    }

    public void inOrder(TreeNode node, int k) {

        if (node.left != null) {
            inOrder(node.left, k);
        }
        // node.val
        depth ++;
        if (depth == k) {
            answer = node.val;
            return;
        }

        if (node.right != null) {
            inOrder(node.right, k);
        }
    }

}


