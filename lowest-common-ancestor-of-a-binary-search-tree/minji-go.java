/**
 * <a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/">week13-2. lowest-common-ancestor-of-a-binary-search-tree</a>
 * <li>Description: find the lowest common ancestor (LCA) node of two given nodes in the BST. </li>
 * <li>Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree </li>
 * <li>Time Complexity: O(H), Runtime 5ms       </li>
 * <li>Space Complexity: O(1), Memory 44.91MB   </li>
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode node = root;
        while (node != null) {
            if (p.val < node.val && q.val < node.val) {
                node = node.left;
            } else if (p.val > node.val && q.val > node.val) {
                node = node.right;
            } else {
                return node;
            }
        }

        throw new IllegalArgumentException();
    }
}
