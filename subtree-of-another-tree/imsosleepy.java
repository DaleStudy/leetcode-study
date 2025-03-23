// 이지문제가 아닌거 같다. 루트 노드를 반복 검증해야하는데 방법을 못 찾아서 오래걸림
// 시간 복잡도는 O(root의 길이*subRoot의 길이)
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        
        if (isSameTree(root, subRoot)) return true;

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean isSameTree(TreeNode a, TreeNode b) {
        if (a == null && b == null) return true; // 둘 다 null이면 같음
        if (a == null || b == null) return false; // 하나만 null이면 다름
        if (a.val != b.val) return false; // 값이 다르면 다름

        // DFS로 지속 검증 
        return isSameTree(a.left, b.left) && isSameTree(a.right, b.right);
    }
}
