// 시간복잡도: 이진검색트리가 균형잡힌 경우 O(logN), 균형잡히지 않은 경우 O(N)
// 공간복잡도: O(1)

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
var lowestCommonAncestor = function(root, p, q) {
    while(root) {
        // root의 값보다 p와 q의 값이 모두 작으면 root를 root.left로 이동
        if (p.val < root.val && q.val < root.val) {
            root = root.left;
        }
        // root의 값보다 p와 q의 값이 모두 크면 root를 root.right로 이동
        else if (p.val > root.val && q.val > root.val) {
            root = root.right;
        }
        else break;
    }
    return root;
};
