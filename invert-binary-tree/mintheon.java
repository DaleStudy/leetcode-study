import java.util.ArrayDeque;
import java.util.Queue;

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
//공간복잡도: O(n)
class Solution {
  public TreeNode invertTree(TreeNode root) {
    if(root == null) {
      return root;
    }

    Queue<TreeNode> queue = new ArrayDeque<>();
    queue.add(root);

    while(!queue.isEmpty()) {
      TreeNode cur = queue.poll();

      if(cur == null) {
        continue;
      }

      TreeNode temp = cur.left;
      cur.left = cur.right;
      cur.right = temp;

      if(cur.left != null) {
        queue.add(cur.left);
      }

      if(cur.right != null) {
        queue.add(cur.right);
      }
    }

    return root;
  }
}
