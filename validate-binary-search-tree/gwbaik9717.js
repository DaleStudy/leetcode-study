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
 * @return {boolean}
 */
var isValidBST = function (root) {
  const dfs = (root) => {
    let minVal = root.val;
    let maxVal = root.val;

    if (root.left) {
      if (root.left.val >= root.val) {
        return false;
      }

      const result = dfs(root.left);

      if (!result) {
        return false;
      }

      const [min, max] = result;

      if (max >= root.val) {
        return false;
      }

      minVal = Math.min(minVal, min);
      maxVal = Math.max(maxVal, max);
    }

    if (root.right) {
      if (root.right.val <= root.val) {
        return false;
      }

      const result = dfs(root.right);

      if (!result) {
        return false;
      }

      const [min, max] = result;

      if (min <= root.val) {
        return false;
      }

      minVal = Math.min(minVal, min);
      maxVal = Math.max(maxVal, max);
    }

    return [minVal, maxVal];
  };

  if (dfs(root)) {
    return true;
  }

  return false;
};
