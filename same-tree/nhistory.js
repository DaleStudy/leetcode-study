/**
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
  // If p and q is null, return true
  if (!p && !q) return true;
  // Compare root and length between p and q
  if (!p || !q || p.val !== q.val) return false;
  // Execute recursive function to search each tree
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

// TC: O(n)
// SC: O(n)
