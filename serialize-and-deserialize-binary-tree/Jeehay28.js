/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

// ✅ Time Complexity: O(N), where N is the number of nodes
// ✅ Space Complexity: O(N)

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */

var serialize = function (root) {
  // Serialization (Tree → String)
  // Uses BFS (level-order traversal) to visit nodes level by level.
  // Stores "null" for missing children to maintain structure.
  // Output format: "1,2,3,null,null,4,5" (comma-separated values).

  if (!root) return "";

  let queue = [root];
  let str = [];

  while (queue.length > 0) {
    let node = queue.shift();

    if (node) {
      str.push(node.val);
      queue.push(node.left);
      queue.push(node.right);
    } else {
      str.push("null");
    }
  }
  return str.join(",");
};

// ✅ Time Complexity: O(N), where N is the number of nodes
// ✅ Space Complexity: O(N)

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function (data) {
  // Deserialization (String → Tree)
  // Splits the serialized string into an array of values.
  // Uses BFS (level-order traversal) to reconstruct the tree.

  if (!data) return null;

  let values = data.split(",");
  let root = new TreeNode(parseInt(values[0])); // // Root node at index 0
  let queue = [root];
  let index = 1; // Start processing children from index 1

  while (queue.length > 0) {
    let node = queue.shift();

    // Process left child (index points to left node value)
    if (values[index] !== "null") {
      node.left = new TreeNode(parseInt(values[index]));
      queue.push(node.left);
    }

    index += 1; // Move to the next position

    // Process right child (ensure index is within bounds)
    if (index < values.length && values[index] !== "null") {
      // Ensure we don't access an index out of bounds
      node.right = new TreeNode(parseInt(values[index]));
      queue.push(node.right);
    }

    index += 1; // Move to the next position
  }

  return root;
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
