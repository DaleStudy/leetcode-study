/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

const NULL_SIGN = 'X';

/**
 * Encodes a tree to a single string.
 * 시간복잡도: O(n)
 * 공간복잡도: O(h) (h: 재귀 스택 깊이 즉 트리 높이)
 * @param {TreeNode} root
 * @return {string}
 */
const serialize = function (root) {
    const result = [];

    function traverse(root) {
        result.push(root?.val ?? NULL_SIGN);
        if (!root) {
            return;
        }
        traverse(root.left);
        traverse(root.right);
    }

    traverse(root);
    return result.join(',');
};

/**
 * Decodes your encoded data to tree.
 * 시간복잡도: O(n)
 * 공간복잡도: O(h) (h: 재귀 스택 깊이 즉 트리 높이)
 * @param {string} data
 * @return {TreeNode}
 */
const deserialize = function (data) {
    const splited = data.split(',');
    let i = 0;

    function makeTree() {
        if (splited[i] === NULL_SIGN) {
            return null;
        }

        const node = new TreeNode(Number(splited[i]));
        i += 1;
        node.left = makeTree();
        i += 1;
        node.right = makeTree();

        return node;
    }

    return makeTree();
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
