/**
 * TC : O(n)
 *   - TreeNode의 노드 수 n 만큼 순회하므로 O(n)
 * SC : O(n)
 *   - TreeNode의 노드 높이 h 만큼 콜스택이 쌓이고, 편향 트리의 경우 O(n) 까지 공간이 필요
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // p와 q 둘다 null 인가?
        if(p == null && q == null) {
            return true;
        } else if(p == null || q == null) { // 하나만 null 인가
            return false;
        } else if(p.val != q.val) {
            return false;
        } else {
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
    }
}
