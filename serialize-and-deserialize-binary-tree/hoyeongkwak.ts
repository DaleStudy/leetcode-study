/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
    /*
    Time complexity: O(n)
    Space complexity: O(n)
    */
    const strArray = []
    const dfs = (node: TreeNode): void => {
        if (node == null) {
            strArray.push('null')
            return
        }
        strArray.push(node.val)
        dfs(node.left)
        dfs(node.right)
    }
    dfs(root)
    return strArray.join(',')
};

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
     /*
    Time complexity: O(n)
    Space complexity: O(n)
    */
    const values = data.split(',')
    let idx = 0
    const dfs = (): TreeNode | null => {
        if (idx >= values.length || values[idx] == 'null') {
            idx++
            return null
        }
        const node = new TreeNode(+values[idx])
        idx++
        node.left = dfs()
        node.right = dfs()
        return node
    }

    return dfs()
};


/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
 
