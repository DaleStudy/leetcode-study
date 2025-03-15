/*
# Time Complexity: O(n)
# Space Complexity: O(n)
  - 재귀 호출 함수의 파라미터 root, depth, ans
*/

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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();

        dfs(root, 0, ans);

        return ans;
    }

    private void dfs(TreeNode root, int depth, List<List<Integer>> ans) {
        if (root == null) return;

        if (ans.size() == depth) {
            ans.add(new ArrayList<>());
        }
        ans.get(depth).add(root.val);

        dfs(root.left, depth + 1, ans);
        dfs(root.right, depth + 1, ans);
    }
}
