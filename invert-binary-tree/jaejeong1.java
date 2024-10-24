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
  // 풀이: child node로 내려가면서 재귀로 계속 left와 right를 바꿔준다.
  // TC: O(N)
  // SC: O(N)
  public TreeNode invertTree(TreeNode root) {
    return invert(root);
  }

  private TreeNode invert(TreeNode node) {
    if (node == null) {
      return node;
    }

    node = swap(node);

    invert(node.left);
    invert(node.right);

    return node;
  }

  private TreeNode swap(TreeNode node) {
    var temp = node.left;
    node.left = node.right;
    node.right = temp;

    return node;
  }
}