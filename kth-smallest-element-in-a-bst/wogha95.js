// TC: O(N)
// SC: O(N)

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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  let result = null;

  dfs(root);

  return result;

  function dfs(current) {
    if (result !== null) {
      return;
    }
    if (!current) {
      return;
    }

    dfs(current.left);
    if (current.val >= 0) {
      if (k === 1) {
        result = current.val;
      }
      k -= 1;
    }
    dfs(current.right);
  }
};
