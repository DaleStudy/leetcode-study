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

// Time Complexity: O(n)
// Space Complexity: O(h) where h is the height of the tree
function maxPathSum(root: TreeNode | null): number {
  let maximumSum = -Infinity;

  const dfs = (node: TreeNode | null) => {
    if (!node) return 0;

    let leftResult = dfs(node.left);
    let rightResult = dfs(node.right);

    leftResult = Math.max(0, leftResult);
    rightResult = Math.max(0, rightResult);

    maximumSum = Math.max(maximumSum, node.val + leftResult + rightResult);

    return node.val + Math.max(leftResult, rightResult);
  };

  dfs(root);

  return maximumSum;
}
