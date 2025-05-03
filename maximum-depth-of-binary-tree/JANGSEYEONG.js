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
  if (!root) return 0; // 노드가 없으면 깊이는 0

  // 현재 노드가 존재하므로 기본 깊이는 1
  // 자식이 아예 없는 경우를 대비해 초기값 설정
  let left = 1;
  let right = 1;

  // 왼쪽 서브트리가 있으면 재귀적으로 깊이 계산 후 현재 레벨(+1) 추가
  if (root.left) {
    left = maxDepth(root.left) + 1;
  }
  // 오른쪽 서브트리가 있으면 재귀적으로 깊이 계산 후 현재 레벨(+1) 추가
  if (root.right) {
    right = maxDepth(root.right) + 1;
  }
  // 왼쪽과 오른쪽 서브트리 중 더 깊은 값을 반환
  return Math.max(left, right);
};
