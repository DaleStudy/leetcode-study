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

// ✔️ Recursive Approach
// Time Complexity: O(N), N = Total number of nodes (each node is processed once)
// Space Complexity: O(H), H = Height of the tree (due to recursion stack depth)

var invertTree = function (root) {
  if (!root) return null;

  [root.left, root.right] = [root.right, root.left];

  invertTree(root.left);
  invertTree(root.right);

  return root;
};

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

// ✔️ Stack → DFS approach
// Time Complexity: O(N), N = Total number of nodes (each node is processed once)
// Space Complexity: O(H), H = Height of the tree (due to recursion stack depth)

// var invertTree = function (root) {
//   let stack = [root];

//   while (stack.length > 0) {
//     const node = stack.pop();
//     if (!node) continue;

//     [node.left, node.right] = [node.right, node.left];
//     stack.push(node.left);
//     stack.push(node.right);
//   }
//   return root;
// };


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

// ✔️ Queue → BFS
// Time Complexity: O(N), N = Total number of nodes (each node is processed once)
// Space Complexity: O(W), W = Maximum width of the tree
// var invertTree = function (root) {
//   let queue = [root];

//   while (queue.length > 0) {
//     const node = queue.shift();
//     if (!node) continue;

//     [node.left, node.right] = [node.right, node.left];
//     queue.push(node.left);
//     queue.push(node.right);
//   }
//   return root;
// };


