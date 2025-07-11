/**
 * <a href="https://leetcode.com/problems/subtree-of-another-tree/">week15-1. subtree-of-another-tree</a>
 * <li>Description: Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot </li>
 * <li>Topics: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function</li>
 * <li>Time Complexity: O(N*M), Runtime 2ms     </li>
 * <li>Space Complexity: O(H), Memory 43.98MB   </li>
 */
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        if (isSameTree(root, subRoot)) return true;
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    public boolean isSameTree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) return true;
        if (root == null || subRoot == null) return false;
        if (root.val != subRoot.val) return false;
        return isSameTree(root.left, subRoot.left) && isSameTree(root.right, subRoot.right);
    }
}
