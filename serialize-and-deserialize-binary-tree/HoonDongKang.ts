/**
 * [Problem]: [297] Serialize and Deserialize Binary Tree
 * (\https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)
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

/*
 * Encodes a tree to a single string.
 */
//시간복잡도 O(N)
//공간복잡도 O(N)
function serialize(root: TreeNode | null): string {
    if (!root) return "NULL";

    const left = serialize(root.left);
    const right = serialize(root.right);

    return `${root.val},${left},${right}`;
}

/*
 * Decodes your encoded data to tree.
 */
//시간복잡도 O(N)
//공간복잡도 O(N)
function deserialize(data: string): TreeNode | null {
    const values = data.split(",");
    let index = 0;

    function dfs(): TreeNode | null {
        if (values[index] === "NULL") {
            index++;
            return null;
        }
        const node = new TreeNode(+values[index++]);

        node.left = dfs();
        node.right = dfs();

        return node;
    }

    return dfs();
}
