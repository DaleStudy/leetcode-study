// 이진 탐색트리는 보통 O(N) ~ O(NlogN)을 요구한다. 
// 그래서 이번에도 모든 노드를 한번만 탐색하는게 목표
// Node.val의 숫자 크기 때문에 Max_VALUE를 잘 지정해주면 바로 풀림
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean isValidBST(TreeNode node, long min, long max) {
        if (node == null) return true; 

        if (node.val <= min || node.val >= max) return false;

        return isValidBST(node.left, min, node.val) &&
               isValidBST(node.right, node.val, max);
    }
}
