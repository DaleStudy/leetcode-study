function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

const buildTree = function (preorder, inorder) {
  if (preorder.length === 0) return null;

  const rootNode = new TreeNode(preorder[0]);
  const rootValueIndexAtInorder = inorder.indexOf(preorder[0]);

  const leftLength = rootValueIndexAtInorder - 0;
  const rightLength = inorder.length - 1 - rootValueIndexAtInorder;

  const leftPreorder = preorder.slice(1, 1 + leftLength);
  const leftInorder = inorder.slice(0, 0 + leftLength);
  rootNode.left = buildTree(leftPreorder, leftInorder);

  const rightPreorder = preorder.slice(
    1 + leftLength,
    1 + leftLength + rightLength
  );
  const rightInorder = inorder.slice(
    rootValueIndexAtInorder + 1,
    rootValueIndexAtInorder + 1 + rightLength
  );
  rootNode.right = buildTree(rightPreorder, rightInorder);

  return rootNode;
};

function bfsTraversal(root) {
  const treeValues = [];

  const queue = [];
  queue.push(root);

  while (queue.length > 0) {
    const n = queue.length;

    for (let i = 0; i < n; i++) {
      const currentNode = queue.shift();

      if (currentNode) {
        treeValues.push(currentNode.val);
        queue.push(currentNode.left);
        queue.push(currentNode.right);
      } else {
        treeValues.push(null);
        queue.push(null);
        queue.push(null);
      }
    }

    if (queue.every((el) => el === null)) break;
  }

  return treeValues;
}

// console.log(bfsTraversal(buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])));
console.log(bfsTraversal(buildTree([1, 2], [2, 1])));
