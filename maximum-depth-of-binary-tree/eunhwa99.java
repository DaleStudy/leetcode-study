public class eunhwa99 {

  // 시간 복잡도: O(n) - 트리를 한 번 순회
  // 공간 복잡도: O(h) - 재귀 호출 스택 공간 (h는 트리의 높이)
  class Solution {
    public int maxDepth(TreeNode root) {
      if (root == null) return 0; // 빈 노드인 경우 깊이는 0
      int leftDepth = maxDepth(root.left); // 왼쪽 서브트리 깊이
      int rightDepth = maxDepth(root.right); // 오른쪽 서브트리 깊이
      return Math.max(leftDepth, rightDepth) + 1; // 최대 깊이 + 1 (현재 노드)
    }
  }
}

