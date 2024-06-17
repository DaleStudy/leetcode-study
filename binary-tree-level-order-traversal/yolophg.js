// Time Complexity: O(n)
// Space Complexity: O(n)

var levelOrder = function (root) {
  // if the root is null, return an empty array.
  if (root === null) return [];

  const result = [];
  const queue = [root];

  // while there are nodes in the queue,
  while (queue.length > 0) {
    const levelSize = queue.length;
    const currentLevel = [];

    // loop nodes in the current level.
    for (let i = 0; i < levelSize; i++) {
      // dequeue the front node.
      const currentNode = queue.shift();
      // add value to the current level array.
      currentLevel.push(currentNode.val);
      // enqueue left child if exists.
      if (currentNode.left) queue.push(currentNode.left);
      // enqueue right child if exists.
      if (currentNode.right) queue.push(currentNode.right);
    }

    // add the current level array to the result.
    result.push(currentLevel);
  }

  return result;
};
