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
  // 풀이 : DFS 탐색을 통해 리프 노드까지 탐색하면서 깊이를 계산한다.
  // TC: O(N), SC: O(N)
  int answer = 0;

  public int maxDepth(TreeNode root) {
    dfs(root, 1);

    return answer;
  }

  private void dfs(TreeNode node, int depth) {
    if (node == null) {
      return;
    }

    if (depth > answer) {
      answer = depth;
    }

    depth++;

    dfs(node.left, depth);
    dfs(node.right, depth);
  }
}
