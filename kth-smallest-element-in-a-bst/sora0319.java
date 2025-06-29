public class Solution {
    private int count = 0;
    private int answer = -1;

    public int kthSmallest(TreeNode root, int k) {
        ordering(root, k);
        return answer;
    }

    private void ordering(TreeNode node, int k) {
        if (node == null) return;
        ordering(node.left, k);
        count++;
        if (count == k) {
            answer = node.val;
            return;
        }
        ordering(node.right, k);
    }
}

