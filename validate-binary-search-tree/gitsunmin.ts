/**
 * https://leetcode.com/problems/validate-binary-search-tree/
 * time complexity : O(n)
 * space complexity : O(n)
 */

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

function validate(node: TreeNode | null, lower: number, upper: number): boolean {
    if (!node) return true;
    const val = node.val;

    if (val <= lower || val >= upper) return false;
    if (!validate(node.right, val, upper)) return false;
    if (!validate(node.left, lower, val)) return false;

    return true;
}

function isValidBST(root: TreeNode | null): boolean {

    return validate(root, -Infinity, Infinity);
}
