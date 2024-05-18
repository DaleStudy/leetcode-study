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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  // Make function to check two triangle is same or not
  const isSame = (root1, root2) => {
    // If both of root1 and root2 is null, return true
    if (!root1 && !root2) return true;
    // If one of root1 and root2 is null or root1.val is not equal to root2.val, return false
    if (!root1 || !root2 || root1.val !== root2.val) return false;
    // Compare each left and right value with recursive
    return isSame(root1.left, root2.left) && isSame(root1.right, root2.right);
  };

  // Make dfs function to check nodes inside of root tree
  const dfs = (node) => {
    // if node is null, return false
    if (!node) return false;
    // Check triangle is equal to subRoot
    if (isSame(node, subRoot)) return true;
    // Check one of the left or right node is same with triangle
    return dfs(node.left) || dfs(node.right);
  };
  // Execute dfs function
  return dfs(root);
};

// TC: O(n*m)
// SC: O(max(m,n))
