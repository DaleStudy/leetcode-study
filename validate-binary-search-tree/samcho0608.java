// link: https://leetcode.com/problems/validate-binary-search-tree/description/
// difficulty: Medium
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
class Solution1 {
    // Problem:
    // * return: check if tree is a valid BST
    // * left subtree contains keys strictly less than node's key
    // * right subtree contains keys strictly greater than node's key
    // * recursive structure
    // Solution:
    // * Time Complexity: O(N)
    // * Space Complexity(in terms of call stack):
    //   * O(N) if skewed
    //   * O(log N) if not skewed
    public boolean isValidBST(TreeNode root) {
        // checklist:
        // * is subtree a valid bst
        // * left subtree : is max value of subtree less than node
        // * right subtree : is min value of subtree greater than node
        return isValid(root, null, null);
    }

    private boolean isValid(TreeNode node, Integer min, Integer max) {
        if(node == null) return true;

        int val = node.val;

        if(min != null && val <= min) return false;
        if(max != null && val >= max) return false;

        if(!isValid(node.left, min, val)) return false;
        if(!isValid(node.right, val, max)) return false;

        return true;
    }
}

// in-order traversal approach
// * reads from left-most to right (strictly increasing val order expected)
class Solution2 {
    private Integer prev;

    // Solution:
    // * Time Complexity: O(N)
    // * Space Complexity(in terms of call stack):
    //   * O(N) if skewed
    //   * O(log N) if not skewed
    public boolean isValidBST(TreeNode root) {
        prev = null;
        return inorder(root);
    }

    private boolean inorder(TreeNode node) {
        // reached end without failure
        if(node == null) return true;

        // inorder so travel left first
        if(!inorder(node.left)) return false;

        // if node value is not greater than prev, it isn't a BST in in-order
        if(prev != null && node.val <= prev) return false;
        prev = node.val;

        return inorder(node.right);
    }
}
