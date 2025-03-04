// 🚀 Iterative approach (No recursion)
// ✅ Time Complexity: O(h), where h is the height of the tree
// ✅ Space Complexity: O(1) (better space efficiency)

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  let node = root;

  while (node) {
    if (p.val < node.val && q.val < node.val) {
      node = node.left;
    } else if (node.val < p.val && node.val < q.val) {
      node = node.right;
    } else {
      return node;
    }
  }
};


// 🚀 Recursive approach
// ✅ Time Complexity: O(h), where h is the height of the tree
// ✅ Space Complexity: O(h) (due to recursion stack)
// 🔍 The function moves down the BST recursively:
//    - If both p and q are smaller, search the left subtree
//    - If both p and q are larger, search the right subtree
//    - Otherwise, root is the LCA

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
// var lowestCommonAncestor = function (root, p, q) {
//   if (p.val < root.val && q.val < root.val) {
//     return lowestCommonAncestor(root.left, p, q);
//   }

//   if (root.val < p.val && root.val < q.val) {
//     return lowestCommonAncestor(root.right, p, q);
//   }

//   return root;
// };

