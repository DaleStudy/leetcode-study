class Solution {
    /* 시간 복잡도: O(N)
    * - 재귀 호출: 트리 노드의 개수(N) 만큼
    * 공간 복잡도: O(N)
    * - 재귀 호출: 트리 노드의 개수(N) 만큼
    */ 
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    boolean validate(TreeNode node, long min, long max) {
        if (node == null) return true;
        if (node.val <= min || node.val >= max) return false;
        return validate(node.left, min, node.val) && validate(node.right, node.val, max);
    }
}

