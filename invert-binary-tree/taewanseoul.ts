/**
 * 226. Invert Binary Tree
 * Given the root of a binary tree, invert the tree, and return its root.
 *
 * https://leetcode.com/problems/invert-binary-tree/description/
 *
 */

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

// O(n) time
// O(n) space
function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) {
    return null;
  }

  const left = invertTree(root.left);
  const right = invertTree(root.right);

  root.left = right;
  root.right = left;

  return root;
}
