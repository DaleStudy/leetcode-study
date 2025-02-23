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

//시간복잡도: O(n)
//공간복잡도: O(1)
class Solution {
  public int maxDepth(TreeNode root) {
    if(root == null) {
      return 0;
    }

    int leftDepth = this.maxDepth(root.left);
    int rightDepth = this.maxDepth(root.right);

    return Math.max(leftDepth, rightDepth) + 1;
  }
}
