/**
 * @description
 * root tree의 각 노드들에서 subRoot의 root와 같으면 preOrder를 통해 일치하는지 확인하는 로직
 *
 * n = count of root node
 * time complexity: O(n^2)
 * space complexity: O(n^2)
 */
var isSubtree = function (root, subRoot) {
  const findTree = (tree, target) => {
    if (!tree && !target) return true;
    if (!tree || !target || tree.val !== target.val) return false;

    if (!findTree(tree.left, target.left)) return false;
    if (!findTree(tree.right, target.right)) return false;

    return true;
  };

  const preOrder = (tree) => {
    if (!tree) return false;

    if (tree.val === subRoot.val) {
      if (findTree(tree, subRoot)) return true;
    }
    if (preOrder(tree.left)) return true;
    if (preOrder(tree.right)) return true;

    return false;
  };

  return preOrder(root);
};
