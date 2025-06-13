/**
 * [Problem]: [124 Binary Tree Maximum Path Sum
 * (https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)
 */
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

//시간복잡도 O(n)
//공간복잡도 O(h)
function maxPathSum(root: TreeNode | null): number {
    if (!root) return 0;
    let result = root.val;

    function dfs(node: TreeNode | null) {
        if (!node) return 0;

        let leftMax = Math.max(dfs(node.left), 0);
        let rightMax = Math.max(dfs(node.right), 0);

        result = Math.max(node.val + leftMax + rightMax, result);

        return node.val + Math.max(leftMax, rightMax);
    }

    dfs(root);
    return result;
}
