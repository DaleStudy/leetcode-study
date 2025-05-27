/**
 * // Definition for a Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {
    if (!node) return null;

    const oldToNew = new Map();

    const dfs = (node) => {
        if (oldToNew.has(node)) {
            return oldToNew.get(node);
        }

        const copy = new _Node(node.val);
        oldToNew.set(node, copy);

        for (let neighbor of node.neighbors) {
            copy.neighbors.push(dfs(neighbor));
        }

        return copy;
    };

    return dfs(node);
};
