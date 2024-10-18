/**
 * @description
 * brainstorming:
 * preorder traverse
 *
 * n = length of root
 * time complexity: O(n)
 * space complexity: O(n)
 */
var invertTree = function (root) {
  const preOrder = (tree) => {
    if (tree === null) return null;

    const currentNode = new TreeNode(tree.val);

    currentNode.right = preOrder(tree.left);
    currentNode.left = preOrder(tree.right);

    return currentNode;
  };

  return preOrder(root);
};
