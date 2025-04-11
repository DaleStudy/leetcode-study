/*
* 시간 복잡도: O(n)
* 공간 복잡도; O(h)
* -> h는 트리의 높이
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
 * @return {boolean}
 */
var isValidBST = function(root) {
  function bst(node , min, max) {
    if (!node) return true;

    if (node.val <= min || node.val >= max) return false;

    return (
      bst(node.left, min, node.val) && helper(node.right, node.val, max)
    );
  }

  return bst(root, -Infinity, Infinity);
};