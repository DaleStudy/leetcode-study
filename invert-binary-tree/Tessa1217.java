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
 * 이진 트리의 root가 주어질 때 이진 트리를 뒤바꾼 후 root를 반환하세요.
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {

        if (root == null) {
            return root;
        }

        TreeNode current = root;

        // 좌우 변경
        TreeNode temp = current.left;
        current.left = invertTree(current.right);
        current.right = invertTree(temp);

        return root;
    }
}

