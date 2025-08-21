// 시간 복잡도: O(n)
//   - n: 트리의 노드 개수
//   - 각 노드를 정확히 한 번씩 방문하므로 O(n)
//
// 공간 복잡도: O(h)
//   - h: 트리의 높이
//   - 재귀 호출 스택에 최대 h개의 함수 호출이 쌓임
//   - 최악의 경우(편향 트리) h = n 이므로 O(n),
//     최선의 경우(균형 트리) h = log n 이므로 O(log n)

class Solution {
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) return 0

        val leftDepth = maxDepth(root.left)
        val rightDepth = maxDepth(root.right)

        return maxOf(leftDepth, rightDepth) + 1
    }
}
