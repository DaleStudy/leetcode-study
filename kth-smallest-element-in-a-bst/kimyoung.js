var kthSmallest = function (root, k) {
  const nums = [];
  function helper(node) { // helper method to traverse the binary tree to map the node values to nums array
    if (!node) return;
    nums.push(node.val);
    if (node.left) helper(node.left); // recursive call to left node if it exists
    if (node.right) helper(node.right); // recursive call to right node if it exists
  }
  helper(root);
  const sorted = nums.sort((a, b) => a - b); // sort the nums array
  return sorted[k - 1]; //  return kth smallest val
};

// space - O(n) - mapping node values into nums array
// time - O(nlogn) - sort
