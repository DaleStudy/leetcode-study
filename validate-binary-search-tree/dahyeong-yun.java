/**
 * 0. 풀이 개요
 *   - 시간복잡도 : O(n)
 *   - 공간복잡도 : O(n)
 */
class Solution {
    /**
     * 1.3 풀이 아이디어
     *   - root의 좌측은 전부 root.value 보다 작아야 하고, 우측은 더 커야함.
     *   - 각 부모 노드에 대해 좌측 자식 노드는 값이 더 작아야 하고, 우측은 더 커야함.
     *   - 이 검증을 매 노드에 반복하여 이진트리 여부를 체크할 수 있음
     *   - 모든 노드의 갯 수를 n 이라고 할 때 n 개의 노드를 모두 1번 방문하므로 O(n)의 시간복잡도를 가짐
     *   - 별도의 자료구조를 생성하지는 않지만, 콜 스택이 쌓인 상태를 감안 했을 때 최악의 경우 O(n)의 공간복잡도를 가짐.
     */
    public boolean isValidBST(TreeNode root) {
        return check(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    boolean check(TreeNode cursor, long min, long max) {
        if(cursor == null) return true; // 노드가 없는 경우 생략
        if(cursor.val <= min || cursor.val >= max) return false;
        return check(cursor.left, min, cursor.val) && check(cursor.right,cursor.val, max);
    }
}
