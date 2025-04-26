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
  // 트리가 비어있는 경우, 깊이는 0
  if (!root) return 0;

  // 왼쪽 서브트리의 최대 깊이를 재귀적으로 계산
  const leftDepth = maxDepth(root.left);

  // 오른쪽 서브트리의 최대 깊이를 재귀적으로 계산
  const rightDepth = maxDepth(root.right);

  // 왼쪽과 오른쪽 중 더 깊은 쪽을 선택하고, 현재 노드를 포함해 +1
  return Math.max(leftDepth, rightDepth) + 1;
};
