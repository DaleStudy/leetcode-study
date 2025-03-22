// ✅ Time Complexity: O(m * n) (due to the substring search), where m is the number of nodes in root and n is the number of nodes in subRoot.
// ✅ Space Complexity: O(m + n)

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
  // Helper function: Serializes a tree into a string representation in a pre-order fashion
  // by visiting the node first, then left and right subtrees. This ensures each node is uniquely
  // represented with its value, and the structure is captured recursively.
  const serialize = (node) => {
    if (!node) return "#"; // Use "#" to represent null nodes, ensuring we capture structure.
    return `(${node.val},${serialize(node.left)},${serialize(node.right)})`; // Recursively serialize left and right children.
  };

  const serializedRoot = serialize(root); // O(m) for serializing root.
  const serializedSubRoot = serialize(subRoot); // O(n) for serializing subRoot.

  return serializedRoot.includes(serializedSubRoot); // O(m * n) for the substring search.
};



// ✅ Time Complexity: O(m * n), where m is the number of nodes in root and n is the number of nodes in subRoot.
// ✅ Space Complexity: O(m + n), due to the recursion stack for both isSubtree and isSameTree.

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
// var isSubtree = function (root, subRoot) {
//   // Base case: if root is null, subRoot can't be a subtree
//   if (!root) return false;

//   // Helper function to check if two trees are identical
//   const isSameTree = (node1, node2) => {
//     if (!node1 && !node2) return true; // Both are null, they are identical
//     if (!node1 || !node2) return false; // One is null, other is not, they are not identical

//     if (node1.val !== node2.val) return false; // Values don't match, not identical

//     // Recursively check both left and right subtrees
//     return (
//       isSameTree(node1.left, node2.left) && isSameTree(node1.right, node2.right)
//     );
//   };

//   // If the current node of root is identical to subRoot, return true
//   if (isSameTree(root, subRoot)) return true;

//   // isSubtree is true if subRoot exists as a subtree in either the left or right side of root.
//   // It checks both sides recursively until it finds a match, and if found, returns true.
//   // If it doesn't find a match in either subtree, it will return false.
//   return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
// };


