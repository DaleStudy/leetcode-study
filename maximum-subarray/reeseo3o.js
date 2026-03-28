/**
 * Time complexity: O(n)
 * Space complexity: O(h) - h is the height of the tree, worst case O(n)
 */
const maxDepth = (root) => {
  if (root === null) return 0;

  const leftDepth = maxDepth(root.left);
  const rightDepth = maxDepth(root.right);

  return 1 + Math.max(leftDepth, rightDepth);
};

// BFS - TC: O(n) | SC: O(n)
const maxDepthBFS = (root) => {
  if (root === null) return 0;

  const queue = [root];
  let depth = 0;

  while (queue.length > 0) {
    const levelSize = queue.length;

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    depth++;
  }

  return depth;
};
