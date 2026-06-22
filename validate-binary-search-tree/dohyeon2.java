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
class Solution {
    // TC : O(n) Each node is visited once in the loop.
    // SC : O(n) Memory allocated for call stack
    // In the first attempt, I tried BFS to solve the problem.
    // But I figured out that I needed to validate a BST recursively.
    // So, I switched to DFS to solve the problem.
    // At first, I compared the node's value with the children's values.
    // And I checked that those values were in the range of min and max.
    // Then, I simplified the approach by
    // comparing the node's value with the min and max values (assisted by ChatGPT).
    public boolean isValidBST(TreeNode root) {
        return dfs(root);
    }

    // Overloading the method to set default arguments
    private boolean dfs(TreeNode node) {
        return dfs(node, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean dfs(TreeNode node, long min, long max) {
        // It's the end of the tree, return true,
        // because the search is valid until this point.
        if (node == null) {
            return true;
        }

        if (node.val <= min) {
            return false;
        }
        if (node.val >= max) {
            return false;
        }

        // All the result of search must be true, if the tree is valid
        return dfs(node.left, min, node.val) && dfs(node.right, node.val, max);
    }
}
