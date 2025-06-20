/**
 * <a href="https://leetcode.com/problems/invert-binary-tree/">week10-1. invert-binary-tree </a>
 * <li>Description: Design an algorithm to serialize and deserialize a binary tree </li>
 * <li>Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree </li>
 * <li>Time Complexity: O(N), Runtime 0ms      </li>
 * <li>Space Complexity: O(N), Memory 41.28MB   </li>
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            TreeNode parent = queue.poll();
            TreeNode temp = parent.left;
            parent.left = parent.right;
            parent.right = temp;
            if (parent.left != null) queue.offer(parent.left);
            if (parent.right != null) queue.offer(parent.right);
        }

        return root;
    }
}
