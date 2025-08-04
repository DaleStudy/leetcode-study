/**
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  let current = root;

  while (current) {
    // 두 노드의 값이 현재 노드보다 모두 작으면 왼쪽 서브트리로 이동
    if (p.val < current.val && q.val < current.val) {
      current = current.left;
    }
    // 두 노드의 값이 현재 노드보다 모두 크면 오른쪽 서브트리로 이동
    else if (p.val > current.val && q.val > current.val) {
      current = current.right;
    }
    // 현재 노드가 분기점이면 그게 LCA!
    else {
      return current;
    }
  }

  return null; // 만약 트리에 없다면 null 반환 (일반적으로 BST에는 항상 존재한다고 가정)
};
