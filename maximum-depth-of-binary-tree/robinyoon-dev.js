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
 * @return {number}
 */
var maxDepth = function (root) {

    //NOTE: 현재 노드의 최대 깊이는 왼쪽 자식 트리의 최대 깊이와 오른쪽 자식 트리의 최대 깊이 중 큰 값에 1(현재 노드)을 더한 값
    if (root === null) {
        return 0;
    }

    const leftDepth = maxDepth(root.left);
    const rightDepth = maxDepth(root.right);

    return Math.max(leftDepth, rightDepth) + 1;
};
