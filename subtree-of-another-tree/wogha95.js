/**
 * tree를 순회하면서 subRoot의 시작값과 동일한 노드를 찾습니다.
 * 찾으면 동일한 트리인지 확인합니다.
 *
 * TC: O(N)
 * 최악의 경우, root tree의 모든 node를 순회합니다.
 *
 * SC: O(N)
 * 최악의 경우, root tree의 모든 node를 순회하기 위해 queue를 사용합니다.
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  const queue = [root];

  while (queue.length > 0) {
    const current = queue.shift();

    if (!current) {
      continue;
    }

    if (current.val === subRoot.val && isSameTree(current, subRoot)) {
      return true;
    }

    if (current.left) {
      queue.push(current.left);
    }

    if (current.right) {
      queue.push(current.right);
    }
  }

  return false;

  function isSameTree(rootA, rootB) {
    if (rootA === null && rootB === null) {
      return true;
    }

    if (rootA === null || rootB === null) {
      return false;
    }

    return (
      rootA.val === rootB.val &&
      isSameTree(rootA.left, rootB.left) &&
      isSameTree(rootA.right, rootB.right)
    );
  }
};
