/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
const isSameTree = function(p, q) {
    if (!p && !q) return true;
    return p?.val === q?.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

// 시간복잡도: O(n)
// 공간복잡도: O(h) (h: 트리의 높이, 즉 재귀 호출 스택)
