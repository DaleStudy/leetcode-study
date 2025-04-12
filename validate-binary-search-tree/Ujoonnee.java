/*
time : O(n)
space : O(n)

최솟값과 최댓값의 범위를 정해 검증한다.
*/

class Solution {
    public boolean isValidBST(TreeNode root) {
        return valid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    boolean valid(TreeNode node, long min, long max) {
        if (node == null) {
            return true;
        }

        if (!(node.val > min && node.val < max)) {
            return false;
        }

        return valid(node.left, min, node.val) && valid(node.right, node.val, max);
    }
}