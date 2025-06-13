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
const maxPathSum = function (root) {
    let max = root.val;

    function getMaxSum(node) {
        if (!node) return 0;

        const leftVal = Math.max(getMaxSum(node.left), 0);
        const rightVal = Math.max(getMaxSum(node.right), 0);

        max = Math.max(node.val + leftVal + rightVal, max);

        return node.val + Math.max(leftVal, rightVal);
    }

    getMaxSum(root);

    return max;
};

// 시간복잡도: O(n)
// 공간복잡도: O(h) (h: 트리의 높이, 즉 재귀 스택 깊이)
