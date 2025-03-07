// 트리 탐색은 깊이 우선 탐색이 공간복잡도가 낮다.
// 모든 노드(리스트)를 O(N)의 시간복잡도를 갖는다.
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
