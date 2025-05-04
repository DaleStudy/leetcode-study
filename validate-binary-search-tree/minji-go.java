/**
 * <a href="https://leetcode.com/problems/validate-binary-search-tree/">week02-5.validate-binary-search-tree</a>
 * <li>Description: determine if it is a valid binary search tree (BST).    </li>
 * <li>Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree    </li>
 * <li>Time Complexity: O(N), Runtime 0ms       </li>
 * <li>Space Complexity: O(N), Memory 43.25MB   </li>
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValid(Integer.MIN_VALUE, Integer.MAX_VALUE, root);
    }

    public boolean isValid(long min, long max, TreeNode node) {
        if(node == null) {
            return true;
        }

        if (node.val < min || node.val > max) {
            return false;
        }

        return isValid(min, (long) node.val - 1, node.left)
            && isValid((long) node.val + 1, max, node.right);
    }

}


