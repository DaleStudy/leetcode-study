/**
 * TC: O(N)
 * SC: O(N)
 */
class Solution {

    public int maxDepth(TreeNode root) {
        return findMax(root, 0);
    }

    public int findMax(TreeNode node, int depth) {
        if (node == null) {
            return depth;
        }
        return Math.max(findMax(node.left, depth + 1), findMax(node.right, depth + 1));
    }
}
