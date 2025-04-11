/**
 * [Problem]: [98] Validate Binary Search Tree
 *
 * (https://leetcode.com/problems/validate-binary-search-tree/description/)
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

function isValidBST(root: TreeNode | null): boolean {
    //시간 복잡도 O(n)
    //공간 복잡도 O(n)
    function dfs(node: TreeNode | null, low: number | null, high: number | null) {
        if (!node) return true;
        if ((low !== null && node.val <= low) || (high !== null && node.val >= high)) {
            return false;
        }

        return dfs(node.left, low, node.val) && dfs(node.right, node.val, high);
    }

    //시간 복잡도 O(n)
    //공간 복잡도 O(n)
    let prev: number | null = null;
    function inOrder(node: TreeNode | null): boolean {
        if (!node) return true;

        if (!inOrder(node.left)) return false;

        if (prev !== null && node.val <= prev) return false;

        prev = node.val;

        return inOrder(node.right);
    }

    // return dfs(root, null, null);
    return inOrder(root);
}
