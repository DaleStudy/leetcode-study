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

function kthSmallest(root: TreeNode | null, k: number): number {
  // SC: O(N)
  const values: number[] = [];

  // TC: O(N)
  const dfs = (node: TreeNode | null) => {
    if (node == null) return;
    dfs(node.left);
    values.push(node.val);
    dfs(node.right);
  };

  // SC: O(h)
  // h: the height of the tree
  dfs(root);

  // TC: O(1)
  return values[k - 1];
}

// TC: O(N)
// SC: O(N)
