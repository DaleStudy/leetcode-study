/**
 * https://leetcode.com/problems/subtree-of-another-tree/description/
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  // If the main tree is empty, it can't contain subRoot
  if (!root) return false;

  // If the trees rooted at current node are the same, return true
  if (isSameTree(root, subRoot)) {
    return true;
  }

  // Otherwise, recursively check left and right subtrees
  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};

function isSameTree(s, t) {
  // If both nodes are null, trees are identical at this branch
  if (!s && !t) return true;

  // If only one is null, trees are not identical
  if (!s || !t) return false;

  // If current node values are different, trees are not identical
  if (s.val !== t.val) return false;

  // Recursively check left and right children
  return isSameTree(s.left, t.left) && isSameTree(s.right, t.right);
}
