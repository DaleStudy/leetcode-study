var levelOrder = function (root) {
  // Edge case: If root is null, return []
  if (root === null) return [];

  // Create result and queue
  let result = [];
  let queue = [root];

  // Iterate while queue.length is exist
  while (queue.length) {
    // Create levelArr and levelSize
    let levelArr = [];
    let levelSize = queue.length;
    // Initiate currentNode from queue by using shift method
    while (levelSize) {
      const currentNode = queue.shift();
      levelArr.push(currentNode.val);
      // If currentNode.left is not null, push into the queue
      if (currentNode.left) queue.push(currentNode.left);
      // If currentNode.right is not null, push into the queue
      if (currentNode.right) queue.push(currentNode.right);

      levelSize--;
    }
    // Push levelArr into result
    result.push(levelArr);
  }
  return result;
};

// TC: O(n)
// SC: O(n)
