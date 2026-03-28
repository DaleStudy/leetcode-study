/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */

// Good solution from Leetcode
// class Solution{
// public int maxDepth(TreeNode root){
// if (root==null) return 0;
// return Math.max(maxDepth(root.left),maxDepth(root.right)) + 1;
// }
// }

class Solution {
    // TC : O(n)
    // SC : O(h) height of tree(DFS), width of tree(BFS)
    public int maxDepth(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode cursor, int depth) {
        if (cursor == null) {
            return depth;
        }
        return Math.max(
                dfs(cursor.left, depth + 1),
                dfs(cursor.right, depth + 1));
    }
}
