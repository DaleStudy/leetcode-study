// 노드 수 v, 간선 e
// 시간복잡도 O(v+e)
// 공간복잡도 O(v+e)

/**
 * // Definition for a _Node.
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
    if (!node) return

    const visited = new Map()
    visited.set(node, new _Node(node.val))

    const que = [node]

    while (que.length) {
        const curNode = que.shift()

        for (neighbor of curNode.neighbors) {
            if (!visited.has(neighbor)) {
                visited.set(neighbor, new _Node(neighbor.val));
                que.push(neighbor)
            }

            visited.get(curNode).neighbors.push(visited.get(neighbor))
        }
    }

    return visited.get(node)
};
