// Time complexity: O(n)
// Space complexity: O(n)

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
  let answer = 0;

  const dfs = (current, depth) => {
    if (!current) {
      return;
    }

    if (answer < depth) {
      answer = depth;
    }

    if (current.left) {
      dfs(current.left, depth + 1);
    }

    if (current.right) {
      dfs(current.right, depth + 1);
    }
  };

  dfs(root, 1);
  return answer;
};
