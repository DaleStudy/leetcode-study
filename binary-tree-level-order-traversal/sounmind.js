/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  const result = [];

  const dfs = (node, level) => {
    if (!node) {
      return;
    }

    if (!result[level]) {
      result[level] = [];
    }

    result[level].push(node.val);

    dfs(node.left, level + 1);
    dfs(node.right, level + 1);
  };

  dfs(root, 0);

  return result;
};

/**
 * Time Complexity: O(n)
 * - The function visits each node exactly once, making it O(n).
 * - Here, n is the number of nodes in the binary tree.
 *
 * Space Complexity: O(n)
 * - The space complexity is determined by the recursion stack.
 * - In the worst case, the recursion stack could store all nodes in the binary tree.
 * - Thus, the space complexity is O(n).
 */
