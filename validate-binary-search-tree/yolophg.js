// Time Complexity: O(n)
// Space Complexity: O(n)

var isValidBST = function (root) {
  if (root === null) {
    return true;
  }

  // initialize a queue for BFS.
  let queue = [];
  queue.push({ node: root, min: -Infinity, max: Infinity });

  while (queue.length > 0) {
    // dequeue the front one.
    let { node, min, max } = queue.shift();

    // check the BST for the current node.
    if (node.val <= min || node.val >= max) {
      return false;
    }

    // enqueue the left child with updated min and max.
    if (node.left !== null) {
      queue.push({ node: node.left, min: min, max: node.val });
    }

    // enqueue the right child with updated min and max.
    if (node.right !== null) {
      queue.push({ node: node.right, min: node.val, max: max });
    }
  }

  return true;
};
