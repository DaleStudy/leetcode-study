/**
 * [Problem]: [572] Subtree of Another Tree
 * (https://leetcode.com/problems/subtree-of-another-tree/description/)
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

//시간복잡도 O(n*m)
//공간복잡도 O(n+m)
function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    const pre = (node: TreeNode | null) => {
        if (!node) return "N";
        return `(${node.val},${pre(node.left)},${pre(node.right)})`;
    };

    return pre(root).includes(pre(subRoot));
}
