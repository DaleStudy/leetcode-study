/**
 * Runtime: 0ms
 * Time Complexity: O(n)
 *
 * Memory: 44.28MB
 * Space Complexity: O(h)
 * - h: 트리의 높이 or 최대 깊이
 *
 * Approach: 재귀를 이용한 DFS 접근법
 * - 루트부터 시작하여 재귀가 시작할 때마다 1로 계산
 * - 트리의 끝에 도달하면 0을 리턴하여 차례대로 남은 깊이를 계산
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;

        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
