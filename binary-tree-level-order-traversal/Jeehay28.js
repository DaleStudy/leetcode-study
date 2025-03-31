// ✅ Time Complexity: O(n), where n is the number of nodes in the tree
// ✅ Space Complexity: O(n)

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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) return [];

  let output = [];
  let queue = [root];

  while (queue.length > 0) {
    let values = [];

    const lengthQueue = queue.length;

    for (let i = 0; i < lengthQueue; i++) {
      const node = queue.shift();
      values.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    output.push(values);
  }
  return output;
};

