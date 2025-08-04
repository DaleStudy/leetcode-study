/**
 * [Problem]: [100] Same Tree
 * (https://leetcode.com/problems/same-tree/description/)
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

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    // 시간복잡도  O(N)
    // 공간복잡도  O(N)
    function recursiveFunc(p: TreeNode | null, q: TreeNode | null): boolean {
        if (!p && !q) return true;
        if (!p || !q) return false;
        if (p.val !== q.val) return false;
        return recursiveFunc(p.left, q.left) && recursiveFunc(p.right, q.right);
    }

    // 시간복잡도  O(N)
    // 공간복잡도  O(N)
    function stackFunc(p: TreeNode | null, q: TreeNode | null): boolean {
        const stack = [[p, q]];
        while (stack.length) {
            const [p, q] = stack.pop()!;
            if (!p && !q) continue;
            if (!p || !q) return false;
            if (p.val !== q.val) return false;

            stack.push([p.left, q.left]);
            stack.push([p.right, q.right]);
        }

        return true;
    }
}
