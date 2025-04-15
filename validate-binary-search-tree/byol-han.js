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
 * @return {boolean}
 */
var isValidBST = function (root) {
  function helper(node, lower = -Infinity, upper = Infinity) {
    if (!node) return true;

    const val = node.val;

    // 현재 노드가 범위를 벗어나면 false
    if (val <= lower || val >= upper) {
      return false;
    }

    // 오른쪽 서브트리: 최소값은 현재 노드 값
    if (!helper(node.right, val, upper)) {
      return false;
    }

    // 왼쪽 서브트리: 최대값은 현재 노드 값
    if (!helper(node.left, lower, val)) {
      return false;
    }

    return true;
  }

  return helper(root);
};
