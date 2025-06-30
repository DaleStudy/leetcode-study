/**
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
const lowestCommonAncestor = function (root, p, q) {
    // 이진탐색트리(BST)의 특징을 활용하여
    // p, q의 값과 root 값을 비교해 p, q가 속한 트리(left/right)를 판단
    if (p.val < root.val && q.val < root.val) {
        return lowestCommonAncestor(root.left, p, q);
    } else if (p.val > root.val && q.val > root.val) {
        return lowestCommonAncestor(root.right, p, q);
    } else {
        return root;
    }
};

// 시간복잡도: O(h) (h: 트리의 높이, 즉 재귀 스택 깊이)
// 공간복잡도: O(h) (h: 트리의 높이, 즉 재귀 스택 깊이)
