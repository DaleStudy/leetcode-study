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
 * @return {TreeNode}
 */
var invertTree = function (root) {
  const dfs = (current) => {
    if (!current) {
      return;
    }

    const temp = current.left;
    current.left = current.right;
    current.right = temp;

    dfs(current.left);
    dfs(current.right);
  };

  dfs(root);

  return root;
};
