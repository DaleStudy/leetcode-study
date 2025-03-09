// 시간복잡도: O(n) - 모든 노드를 한번씩 방문
// 공간복잡도: O(logn) - 균형 트리인 경우 / O(n) - 한쪽으로 치우친 트리인 경우
// 풀이: 재귀적으로 트리를 순회하면서 두 트리의 노드 값이 같은지 확인

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
var isSameTree = function(p, q) {
    if (p === null && q === null) return true;

    if (p === null || q === null) return false;

    if (p.val != q.val) return false;

    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
