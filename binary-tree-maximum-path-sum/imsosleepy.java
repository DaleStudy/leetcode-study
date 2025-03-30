// dfs와 분할 정복법으로 해결되는 문제
// dfs인 것을 알았으나 모든 숫자가 음수일 경우를 판별하지 못해 GPT에게 도움을 처함
class Solution {
    private int maxSum = Integer.MIN_VALUE; // 전체 최대 경로 합 저장

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return maxSum;
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0; // base case

        // 왼쪽, 오른쪽 서브트리의 최대 경로 합 (음수는 포함 X → Math.max(0, value))
        int left = Math.max(0, dfs(node.left));
        int right = Math.max(0, dfs(node.right));

        // 현재 노드를 포함한 최대 경로 (왼쪽 + 루트 + 오른쪽)
        int pathSum = left + node.val + right;

        // 최대 경로 값 갱신
        maxSum = Math.max(maxSum, pathSum);

        // ✅ 현재 노드를 포함하는 최대 경로 값만 반환해야 함 (연결 가능한 경로)
        return node.val + Math.max(left, right);
    }
}
