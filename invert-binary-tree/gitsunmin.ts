/**
 * https://leetcode.com/problems/invert-binary-tree/
 * time complexity : O(n)
 * space complexity : O(log N)
 */

class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

export const dfs = (root: TreeNode | null, inverted: TreeNode | null): TreeNode | null => {
    if (!root) return null;

    const left = dfs(root.left, inverted);
    const right = dfs(root.right, inverted);

    root.left = right;
    root.right = left;

    return root;
};

function invertTree(root: TreeNode | null): TreeNode | null {
    if (!root) return null;

    return dfs(root, new TreeNode(0));
};
