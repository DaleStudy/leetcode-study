/**
 * WEEK12
 * https://leetcode.com/problems/same-tree/description/
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  // 둘 다 null이면 같은 트리
  if (p === null && q === null) return true;

  // 하나는 null이고 하나는 값이 있다면 다른 트리
  if (p === null || q === null) return false;

  // 값이 다르면 다른 트리
  if (p.val !== q.val) return false;

  // 왼쪽과 오른쪽 서브트리도 각각 재귀적으로 비교
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
