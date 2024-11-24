/**
 * TC: O(N)
 * SC: O(N)
 * N: total count of tree nodes
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
var isValidBST = function (root) {
  return isValidBSTWithBoundary(
    root,
    Number.MIN_SAFE_INTEGER,
    Number.MAX_SAFE_INTEGER
  );

  function isValidBSTWithBoundary(current, min, max) {
    if (!current) {
      return true;
    }

    if (current.val <= min || max <= current.val) {
      return false;
    }

    return (
      isValidBSTWithBoundary(current.left, min, current.val) &&
      isValidBSTWithBoundary(current.right, current.val, max)
    );
  }
};
