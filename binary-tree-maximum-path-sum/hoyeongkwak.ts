/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/*
Time complexity: O(N)
Space complexity: O(N) h: 트리의 높이
*/
function maxPathSum(root: TreeNode | null): number {
    let maxSum = -Infinity
    const dfs = (node: TreeNode): number => {
        if (node == null) return 0

        const leftMax = Math.max(0, dfs(node.left))
        const rightMax = Math.max(0, dfs(node.right))
        const currentMax = node.val + leftMax + rightMax

        maxSum = Math.max(maxSum, currentMax)
        return node.val + Math.max(leftMax, rightMax)
    }
    dfs(root)
    return maxSum
};
