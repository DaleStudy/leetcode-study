/**
 * TC: O(M * N) - N: 메인 트리(root)의 노드 수, M: 서브 트리(subtree)의 노드 수
 * SC: O(M + N)
 * - isSubtree() 콜 스택은 최대 N 개 발생할 수 있고,
 * - 각각 isSameTree() 콜 스택(M 개)을 더한 값까지 늘어날 수 있다.
 * = isSameTree() 콜 스택은 호출 이후 사라지므로, 공간 복잡도는 최대 M + N 이다.
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
