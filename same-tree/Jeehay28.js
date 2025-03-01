// 🚀 Iterative DFS (Stack)
// ✅ Time Complexity: O(n), where n is the number of nodes in the tree
// ✅ Space Complexity: O(n) (worst case), O(log n) (best case for balanced trees)

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  let stack = [[p, q]];
  while (stack.length > 0) {
    const [p, q] = stack.pop();

    if (p === null && q === null) continue;

    if (p === null || q === null) return false;

    if (p.val !== q.val) return false;

    stack.push([p.left, q.left]);
    stack.push([p.right, q.right]);
  }

  return true;
};



// 🚀 recursive approach
// ✅ Time Complexity: O(n), where n is the number of nodes in the tree
// ✅ Space Complexity: O(n) (worst case), O(log n) (best case for balanced trees)

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
// var isSameTree = function (p, q) {
//   // Base case: If both trees are empty, they are the same
//   if (p === null && q === null) return true;

//   // If one of the trees is empty and the other is not, return false
//   if (p === null || q === null) return false;

//   // Compare the values of the current nodes
//   if (p.val !== q.val) return false;

//   // Recursively compare the left and right subtrees
//   return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
// };


