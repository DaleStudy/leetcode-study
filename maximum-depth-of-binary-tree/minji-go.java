/**
 * <a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/">week4-2.maximum-depth-of-binary-tree</a>
 * <li>Description: Given the root of a binary tree, return its maximum depth.</li>
 * <li>Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree</li>
 * <li>Time Complexity: O(N), Runtime 1ms</li>
 * <li>Space Complexity: O(W), Memory 43.21MB</li>
 */

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        int depth = 0;
        while (!queue.isEmpty()) {
            depth++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        return depth;
    }
}
