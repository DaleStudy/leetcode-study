/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  if (!p && !q) {
    return true;
  }

  if (!p || !q || p.val !== q.val) {
    return false;
  }

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

/**
 * Time Complexity: O(n)
 * Reason: We visit each node exactly once.
 *
 * Space Complexity: O(n)
 * Reason:
 *  The space used by the call stack is proportional
 *  to the height of the tree.
 */
