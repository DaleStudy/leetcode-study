// Time Complexity: O(n)
// Space Complexity: O(n)

var kthSmallest = function (root, k) {
  let stack = [];
  let current = root;
  let count = 0;

  while (stack.length > 0 || current !== null) {
    // go to the leftmost node
    while (current !== null) {
      stack.push(current);
      current = current.left;
    }

    // pop the node from the stack
    current = stack.pop();
    count++;

    // if reached the kth node
    if (count === k) {
      return current.val;
    }

    // go to the right node
    current = current.right;
  }

  // if k is out of the range of the number of in the tree
  return null;
};
