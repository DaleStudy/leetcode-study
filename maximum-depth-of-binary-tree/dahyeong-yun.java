/**
 * [풀이 개요]
 * - 시간복잡도 : O(n) : 트리의 모든 노드를 방문해야 함
 * - 공간복잡도 : O(h) : 재귀의 콜 스택은 트리의 높이(h) 만큼 쌓임
 */
class Solution {
    /**
     * [문제 풀이 아이디어]
     * - 이진 트리의 최대 레벨을 구하는 문제
     * - 루트만 존재해도 레벨은 1암.
     * - 자식 노드를 재귀적으로 조회하면서 레벨을 1씩 늘리고, 최대값을 갱신하므로 편향 트리라도 최대값으로 갱신됨.
     */
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
