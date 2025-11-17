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
    // Time Complexity: O(n), n: the number of nodes
    // Space Complexity: O(w), w: max width of tree

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> results = new ArrayList<>();
        if (root == null) return results;

        Queue<TreeNode> levelQueue = new LinkedList<>();    // use queue considering FIFO
        levelQueue.offer(root);

        while (!levelQueue.isEmpty()) {
            ArrayList<Integer> level = new ArrayList<>();   // node values list for each level
            int size = levelQueue.size();

            for (int i = 0; i < size; ++i) {
                TreeNode node = levelQueue.poll();
                level.add(node.val);
                if(node.left != null) levelQueue.offer(node.left);
                if(node.right != null) levelQueue.offer(node.right);
            }

            results.add(level);
        }

        return results;
    }
}
