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
 * @return {TreeNode}
 */
var invertTree = function (root) {
  // Check root is null
  if (!root) return null;
  // Create left and right variable to make recurrsive
  let left = root.left;
  let right = root.right;
  // Execute invertTree functino
  root.left = invertTree(right);
  root.right = invertTree(left);
  return root;
};

// TC: O(n)
// SC: O(n)
