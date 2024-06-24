var buildTree = function (preorder, inorder) {
  // Edge case: if either preorder or inorder is empty, return null
  if (!preorder.length || !inorder.length) return null;

  // The first element in preorder is the root of the tree
  // Find the index of the root in the inorder array
  const root = new TreeNode(preorder[0]);
  const mid = inorder.indexOf(root.val);

  root.left = buildTree(preorder.slice(1, mid + 1), inorder.slice(0, mid));
  root.right = buildTree(preorder.slice(mid + 1), inorder.slice(mid + 1));

  return root;
};

// TC: O(n^2)
// SC: O(n)
