/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  if (!root) return false;

  const isSameTree = (root: TreeNode | null, subRoot: TreeNode | null): boolean => {
    if (!root && !subRoot) return true;
    if (!root || !subRoot) return false;
    if (root.val !== subRoot.val) return false;

    return isSameTree(root.left, subRoot.left) && isSameTree(root.right, subRoot.right);
  };

  const current = isSameTree(root, subRoot);
  const left = isSubtree(root.left, subRoot);
  const right = isSubtree(root.right, subRoot);

  return current || left || right;
}
