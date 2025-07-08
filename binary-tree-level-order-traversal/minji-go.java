/**
 * <a href="https://leetcode.com/problems/binary-tree-level-order-traversal/">week14-2. binary-tree-level-order-traversal</a>
 * <li>Description: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)</li>
 * <li>Topics: Tree, Breadth-First Search, Binary Tree</li>
 * <li>Time Complexity: O(N), Runtime 1ms       </li>
 * <li>Space Complexity: O(N), Memory 45.3MB    </li>
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return Collections.emptyList();
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        List<List<Integer>> results = new ArrayList<>();
        while (!queue.isEmpty()) {
            List<Integer> result = new ArrayList<>();

            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                result.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            results.add(result);
        }

        return results;
    }
}
