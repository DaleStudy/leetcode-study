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
  // Check root is null or not
  if (root === null) {
    return 0;
  }
  // Make queue array to store root and depth variable
  let queue = [root];
  let depth = 0;
  // Iterate until there is an element inside of queue
  while (queue.length > 0) {
    // Record level size to avoid fault size measuring
    let levelSize = queue.length;

    for (let i = 0; i < levelSize; i++) {
      // Grasp first element from the queue
      const node = queue.shift();
      // Push the left node into the queue
      if (node.left) {
        queue.push(node.left);
      }
      // Push the right node into the queue
      if (node.right) {
        queue.push(node.right);
      }
    }
    // Increase depth value
    depth++;
  }

  return depth;
};

// TC: O(n)
// SC: O(n)
