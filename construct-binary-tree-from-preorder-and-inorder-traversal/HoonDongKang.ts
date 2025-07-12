/**
 * [Problem]: [105] Construct Binary Tree From Preorder And Inorder Traversal
 * (https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
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

//시간복잡도 O(n)
//공간복잡도 O(n)
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    if (!preorder.length || !inorder.length) return null;

    const map = new Map<number, number>();
    let idx = 0;

    inorder.forEach((v, i) => map.set(v, i));

    function dfs(left: number, right: number): TreeNode | null {
        if (left > right) return null;

        const value = preorder[idx++];
        const root = new TreeNode(value);
        const index = map.get(value)!;

        root.left = dfs(left, index - 1);
        root.right = dfs(index + 1, right);

        return root;
    }

    return dfs(0, inorder.length - 1);
}
