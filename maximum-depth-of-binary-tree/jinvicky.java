// 왼쪽 서브트리를 모두 탐색한 다음 오른쪽 서브트리 탐색을 시작
//     1 (root)
//     / \
//    2   3
//   / \ / \
//  4  5 6  7
//
// root를 인자로 받아서 노드별로 left, right을 또 재귀로 호출하니
// (1)의 left, right, (2)의 left, right, (3)의 left, right, (4)의 left, right이 실행된다.
// 결과적으로 왼쪽 서브트리의 최대 depth와 오른쪽 서브트리의 최대 depth + 최초 root의 depth 1을 합해서 완성
// Math.max()는 함수 안의 모든 값이 계산되어야만 실행된다.
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
