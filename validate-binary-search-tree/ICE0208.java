class Solution {
    /*
     * 현재 노드가 허용된 범위 안에 있는지 확인한다.
     *
     * 왼쪽 자식은 현재 노드보다 작아야 하므로,
     * upperBound를 현재 노드 값으로 줄인다.
     *
     * 오른쪽 자식은 현재 노드보다 커야 하므로,
     * lowerBound를 현재 노드 값으로 올린다.
     *
     * 시간 복잡도: O(n)
     * - n은 전체 노드의 개수
     * - 모든 노드를 한 번씩 검사한다.
     *
     * 공간 복잡도: O(h)
     * - h는 트리의 높이
     * - 재귀 호출 스택이 현재 탐색 중인 경로만큼 쌓인다.
     * - 균형 잡힌 트리라면 O(log n) / 한쪽으로 치우친 트리라면 O(n)
     */
    private boolean isValidWithinRange(TreeNode node, long lowerBound, long upperBound) {
        if (node == null) {
            return true;
        }

        // BST는 중복 값을 허용하지 않으므로 경계값과 같아도 false다.
        if (node.val <= lowerBound || node.val >= upperBound) {
            return false;
        }

        return isValidWithinRange(node.left, lowerBound, node.val)
            && isValidWithinRange(node.right, node.val, upperBound);
    }

    public boolean isValidBST(TreeNode root) {
        return isValidWithinRange(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}
