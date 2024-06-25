// Time Complexity: O(n)
// Space Complexity: O(n)

var buildTree = function (preorder, inorder) {
  // build a map for quick lookup of index positions in inorder array
  // map to store the value -> index relationships
  let map = new Map();
  inorder.forEach((value, index) => map.set(value, index));

  // recursive function to construct the binary tree
  function buildTreeHelper(preStart, preEnd, inStart, inEnd) {
    // if there are no elements to consider
    if (preStart > preEnd || inStart > inEnd) return null;

    // the first element in preorder is the root of the current tree
    let rootValue = preorder[preStart];
    // create a new root node
    let root = { val: rootValue, left: null, right: null };

    // find the root in the inorder array to split the tree
    let inRootIndex = map.get(rootValue);
    // number of nodes in the left subtree
    let numsLeft = inRootIndex - inStart;

    // recursively build the left subtree
    root.left = buildTreeHelper(
      preStart + 1,
      preStart + numsLeft,
      inStart,
      inRootIndex - 1
    );

    // recursively build the right subtree
    root.right = buildTreeHelper(
      preStart + numsLeft + 1,
      preEnd,
      inRootIndex + 1,
      inEnd
    );

    return root;
  }

  // initiate the recursive construction
  return buildTreeHelper(0, preorder.length - 1, 0, inorder.length - 1);
};
