/**
 * [Problem]: [235] Lowest Common Ancestor of a Binary Search Tree
 * (https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)
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

function lowestCommonAncestor(
    root: TreeNode | null,
    p: TreeNode | null,
    q: TreeNode | null
): TreeNode | null {
    //시간복잡도 O(h)
    //공간복잡도 O(h)
    function recursiveFunc(
        root: TreeNode | null,
        p: TreeNode | null,
        q: TreeNode | null
    ): TreeNode | null {
        if (!p || !root || !q) return null;
        if (p.val < root.val && q.val < root.val) {
            return recursiveFunc(root.left, p, q);
        }
        if (root.val < p.val && root.val < q.val) {
            return recursiveFunc(root.right, p, q);
        }

        return root;
    }

    //시간복잡도 O(h)
    //공간복잡도 O(1)
    function loopFunc(
        root: TreeNode | null,
        p: TreeNode | null,
        q: TreeNode | null
    ): TreeNode | null {
        if (!p || !q || !root) return null;

        let node = root;

        while (node) {
            if (p.val < node.val && q.val < node.val) {
                node = node?.left!;
            } else if (p.val > node.val && q.val > node.val) {
                node = node?.right!;
            } else {
                return node;
            }
        }

        return null;
    }
}
