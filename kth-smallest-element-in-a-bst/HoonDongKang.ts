/**
 * [Problem]: [230] Kth Smallest Element in a BST
 * (https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)
 */

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

function kthSmallest(root: TreeNode | null, k: number): number {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function inOrderFunc(root: TreeNode | null, k: number): number {
        const values: number[] = [];

        function dfs(node: TreeNode | null) {
            if (!node) return;
            dfs(node.left);
            values.push(node.val);
            dfs(node.right);
        }

        dfs(root);

        return values[k - 1];
    }
}
