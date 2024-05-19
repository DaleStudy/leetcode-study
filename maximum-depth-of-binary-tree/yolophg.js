// Time complexity : O(n)
// Space complexity : O(n)

var maxDepth = function (root) {
  // if the root is null, the depth is 0.
  if (root === null) {
    return 0;
  }

  // initialize the stack with the root node and its depth, which is 1.
  const stack = [{ node: root, depth: 1 }];
  let maxDepth = 0;

  // process the stack till it is empty.
  while (stack.length > 0) {
    // pop the top element from the stack.
    const { node, depth } = stack.pop();

    if (node !== null) {
      // update the maximum depth.
      maxDepth = Math.max(maxDepth, depth);

      // push the left and right children with their respective depths.
      if (node.left !== null) {
        stack.push({ node: node.left, depth: depth + 1 });
      }
      if (node.right !== null) {
        stack.push({ node: node.right, depth: depth + 1 });
      }
    }
  }

  return maxDepth;
};
