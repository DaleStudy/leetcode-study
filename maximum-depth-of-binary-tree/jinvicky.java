class Solution {
    // 최대 깊이를 탐색하는 것이므로 BFS보다 DFS가 더 적절합니다.
    // 매 노드의 left, right을 재귀로 호출해서 최대 깊이를 반환합니다. 재귀 함수 필요.
    public int maxDepth(TreeNode root) {
        // 재귀 종료 조건 == left 혹은 right가 null일 때, root 자체가 널이라면?
        if (root == null) return 0;

        // 누적을 위해서 1+를 하고, Math.max()로 최댓값을 구합니다.
        return 1+ Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
