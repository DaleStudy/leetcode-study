/**
 * [Problem]: [102] Binary Tree Level Order Traversal
 * (https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
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

// 시간복잡도 O(n)
// 공간복잡도 O(n)
function levelOrder(root: TreeNode | null): number[][] {
    if (!root) return [];

    const result: number[][] = [];
    const queue: TreeNode[] = [root];

    while (queue.length > 0) {
        const level = queue.length;
        const values: number[] = [];

        for (let i = 0; i < level; i++) {
            const node = queue.shift()!;
            values.push(node.val);

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        result.push(values);
    }

    return result;
}
