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
var maxDepth = function (root) {
  if (root === null) {
    return 0;
  }

  const leftDepth = maxDepth(root.left);
  const rightDepth = maxDepth(root.right);

  return Math.max(leftDepth, rightDepth) + 1;
};

/**
 * Time Complexity: O(n), where n is the number of nodes in the binary tree.
 * Reason:
 *  the function visits each node exactly once in order to compute the depth of the tree,
 *  which ensures that each node is processed a single time.
 *
 * Space Complexity: O(h), where h is the height of the binary tree.
 * Reason:
 *   The recursion stack used during the depth-first traversal.
 *
 *   In the worst case, where the tree is completely unbalanced,
 *   the height h can be equal to the number of nodes n, leading to a space complexity of O(n).
 *
 *   In the best case, where the tree is balanced, the height h is log(n),
 *   leading to a space complexity of O(log(n)).
 */
