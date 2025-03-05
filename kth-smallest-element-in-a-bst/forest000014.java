/*
# Time Complexity: O(n)
# Space Complexity: O(n)

heap을 사용한 풀이, in-order traversal을 사용한 풀이 풀어볼 것!
*/
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
    public int kthSmallest(TreeNode root, int k) {
        Map<TreeNode, Integer> sizes = new HashMap<>();

        calculateSize(root, sizes);

        return findKth(root, k, sizes);
    }

    private int calculateSize(TreeNode root, Map<TreeNode, Integer> sizes) {
        if (root == null) return 0;

        int left = calculateSize(root.left, sizes);
        int right = calculateSize(root.right, sizes);

        sizes.put(root, left + right + 1);
        return left + right + 1;
    }

    private int findKth(TreeNode root, int k, Map<TreeNode, Integer> sizes) {
        int left = (root.left == null) ? 0 : sizes.get(root.left);
        int right = (root.right == null) ? 0 : sizes.get(root.right);

        if (left == k - 1) {
            return root.val;
        } else if (left >= k) {
            return findKth(root.left, k, sizes);
        } else {
            return findKth(root.right, k - left - 1, sizes);
        }
    }
}
