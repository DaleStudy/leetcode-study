/**
 * TC: O(M * N) - M: 메인 트리(root)의 노드 수, N: 서브 트리(subtree)의 노드 수
 * SC: O(N) - N: 메인 트리(root)의 높이
 */
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) {
            return false;
        }
        if (isSameTree(root, subRoot)) {
            return true;
        }
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    public boolean isSameTree(TreeNode n1, TreeNode n2) {
        if (n1 == null || n2 == null) {
            return n1 == n2;
        }
        if (n1.val != n2.val) {
            return false;
        }
        return isSameTree(n1.left, n2.left) && isSameTree(n1.right, n2.right);
    }
}
