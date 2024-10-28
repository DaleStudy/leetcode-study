/**
 * @description
 * 두개의 트리를 동시에 순회한다를 초점으로 문제접근하여 풀이
 *
 * n = minimum tree node count of p or q
 * time complexity: O(n)
 * space complexity: O(1)
 */
var isSameTree = function (p, q) {
  const preOrder = (tree1, tree2) => {
    if (!tree1 && !tree2) return true;
    if (!tree1 || !tree2) return false;

    if (tree1.val !== tree2.val) return false;
    if (!preOrder(tree1.left, tree2.left)) return false;
    if (!preOrder(tree1.right, tree2.right)) return false;

    return true;
  };

  return preOrder(p, q);
};
