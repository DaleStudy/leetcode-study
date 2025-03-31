// ✅ Time Complexity: O(N) (Each node is visited once)
// ✅ Space Complexity: O(N)

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
 * @return {number}
 */
var maxPathSum = function (root) {
  let maxSum = -Infinity;

  const dfs = (node) => {
    if (!node) return 0;

    let leftMax = Math.max(dfs(node.left), 0);
    let rightMax = Math.max(dfs(node.right), 0);

    // Compute best path sum that passes through this node
    let currentMax = node.val + leftMax + rightMax;

    // Update global maxSum
    maxSum = Math.max(maxSum, currentMax); // represents the best path sum for the current node.

    return node.val + Math.max(leftMax, rightMax); // propagates the maximum path sum to the parent node.
  };

  dfs(root);
  return maxSum;
};

