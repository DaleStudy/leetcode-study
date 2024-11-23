// class TreeNode {
//   val: number;
//   left: TreeNode | null;
//   right: TreeNode | null;
//   constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//     this.val = val === undefined ? 0 : val;
//     this.left = left === undefined ? null : left;
//     this.right = right === undefined ? null : right;
//   }
// }

/**
 * https://leetcode.com/problems/validate-binary-search-tree
 * T.C. O(n)
 * S.C. O(n)
 */
function isValidBST(root: TreeNode | null): boolean {
  return validate(root, null, null);
}

function validate(node: TreeNode | null, min: number | null, max: number | null): boolean {
  if (!node) return true;
  if (min !== null && node.val <= min) return false;
  if (max !== null && node.val >= max) return false;
  return validate(node.left, min, node.val) && validate(node.right, node.val, max);
}
