/**
 * 문제 요약: 이진 트리의 루트 노드가 주어질 때, 이 트리의 최대 깊이를 반환해야 한다
 * 최대 깊이: 루트 노드에서 가장 먼 리프 노드까지의 경로에 있는 노드의 수
 * 시간 복잡도: O(n) - 모든 노드를 한 번씩 방문
 * 공간 복잡도: O(h) - h는 트리의 높이(최악의 경우 O(n)) - 재귀 호출 스택 사용
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  // 기저 조건: 노드가 없으면(empty tree) 깊이는 0
  if (root === null) {
    return 0;
  }

  const leftDepth = maxDepth(root.left);
  const rightDepth = maxDepth(root.right);

  // 현재 노드의 최대 깊이: 왼쪽과 오른쪽 서브트리의 최대 깊이 중 큰 값에 1을 더한 값
  return Math.max(leftDepth, rightDepth) + 1;
};
