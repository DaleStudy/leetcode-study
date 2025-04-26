/**
 * [Problem]: [104] Maximum Depth of Binary Tree
 *
 * (https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)
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

function maxDepth(root: TreeNode | null): number {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function stackFunc(root: TreeNode | null): number {
        if (!root) return 0;
        let max = 0;
        const stack: [TreeNode, number][] = [[root, 1]];

        while (stack.length > 0) {
            const [node, depth] = stack.pop()!;
            max = Math.max(max, depth);

            if (node.left) stack.push([node.left, depth + 1]);
            if (node.right) stack.push([node.right, depth + 1]);
        }

        return max;
    }

    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function recursiveFunc(root: TreeNode | null): number {
        if (!root) return 0;

        return 1 + Math.max(recursiveFunc(root.left), recursiveFunc(root.right));
    }

    return recursiveFunc(root);
}
