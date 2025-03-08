// 🚀 Optimized Approach: Inorder Traversal (BST Property)
// ✅ Time Complexity: O(n), n represents the number of nodes
// ✅ Space Complexity: O(n), due to recursion stack (in the worst case, e.g., unbalanced tree)

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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  // Correct Order in BST Inorder Traversal: 🌿 (left) → 🌟 (current) → 🌳 (right)
  // 🌿 Go Left (visit the smallest values first).
  // 🌟 Visit Current Node (increment count++).
  // 🌳 Go Right (visit larger values).

  let count = 0;
  let result = null;

  const inorder = (node) => {
    if (!node || result !== null) return; // If node is null or result is found, stop recursion

    inorder(node.left);

    count += 1; // Visit current node
    if (count === k) {
      result = node.val;
      return;
    }

    inorder(node.right);
  };

  inorder(root);

  return result;
};


// 😊 My initial approach
// 🐌This is not optimal for a BST, but it works.
// ✅ Time Complexity: O(n * logn), n represents the number of nodes
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
 * @param {number} k
 * @return {number}
 */
// var kthSmallest = function (root, k) {
//   let arr = [];
//   const dfs = (node) => {
//     if (!node) return null;

//     if (node.val !== undefined) {
//       arr.push(node.val);
//       dfs(node.left);
//       dfs(node.right);
//     }
//   };

//   dfs(root);

//   arr.sort((a, b) => a - b);

//   return arr[k - 1];
// };
