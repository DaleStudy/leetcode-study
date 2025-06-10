/**
 * [Problem]: [226] Invert Binary Tree
 * (https://leetcode.com/problems/invert-binary-tree/)
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

function invertTree(root: TreeNode | null): TreeNode | null {
    // 시간복잡도 O(n)
    // 공간복잡도 O(n)
    function recursiveFunc(root: TreeNode | null): TreeNode | null {
        if (root === null) {
            return null;
        }

        const temp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(temp);

        return root;
    }
    // 시간복잡도 O(n)
    // 공간복잡도 O(n)
    function stackFunc(root: TreeNode | null): TreeNode | null {
        if (root === null) {
            return null;
        }

        const stack: Array<TreeNode | null> = [root];

        while (stack.length > 0) {
            const node = stack.pop()!;

            if (node === null) {
                continue;
            }

            [node.left, node.right] = [node.right, node.left];
            stack.push(node.left, node.right);
        }

        return root;
    }
}
