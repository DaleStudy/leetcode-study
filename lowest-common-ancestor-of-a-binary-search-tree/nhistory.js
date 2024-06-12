var lowestCommonAncestor = function (root, p, q) {
  // Iterate if statement with comparing values
  while (root) {
    if (root.val < p.val && root.val < q.val) root = root.right;
    else if (root.val > p.val && root.val > q.val) root = root.left;
    else return root;
  }
};

// TC: O(n)
// SC: O(1)
