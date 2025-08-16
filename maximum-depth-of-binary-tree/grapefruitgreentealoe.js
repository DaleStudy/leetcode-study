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
  if (!root) return 0;

  // 왼쪽과 오른쪽 서브트리의 최대 깊이를 구한다.
  const leftDepth = maxDepth(root.left);
  const rightDepth = maxDepth(root.right);

  // 현재 노드의 깊이는 왼쪽과 오른쪽 깊이 중 큰 값에 1을 더한 값이다.
  return Math.max(leftDepth, rightDepth) + 1;
};
