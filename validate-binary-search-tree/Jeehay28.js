// ✅ Time Complexity: O(N), where N is the number of nodes in the tree.
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
 * @return {boolean}
 */
var isValidBST = function (root) {
  // Helper function to check BST validity
  const dfs = (node, low, high) => {
    // Base case: Empty subtree is valid
    if (!node) return true;

    if (!(low < node.val && node.val < high)) return false;

    return dfs(node.left, low, node.val) && dfs(node.right, node.val, high);
  };

  return dfs(root, -Infinity, Infinity);
};

