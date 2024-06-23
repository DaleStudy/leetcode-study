// Time Complexity: O(n)
// Space Complexity: O(1)

var lowestCommonAncestor = function (root, p, q) {
  // start from the root.
  let current = root;

  // traverse the tree.
  while (current !== null) {
    // if both p and q are greater than current node, LCA lies in the right.
    if (p.val > current.val && q.val > current.val) {
      current = current.right;
    }
    // if both p and q are smaller than current node, LCA lies in the left.
    else if (p.val < current.val && q.val < current.val) {
      current = current.left;
    }
    // if one of p or q is on one side and the other is on the other side, It's LCA.
    else {
      return current;
    }
  }

  // if the tree is empty.
  return null;
};
