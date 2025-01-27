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
var cloneGraph = function (node) {
    const nodeMap = new Map();

    const dfs = (nodeParam) => {
        if (!nodeParam) {
            return null;
        }

        if (nodeMap.has(nodeParam.val)) {
            return nodeMap.get(nodeParam.val);
        }

        const clone = new Node(nodeParam.val);

        nodeMap.set(clone.val, clone);

        for (const nei of nodeParam.neighbors) {
            clone.neighbors = [...clone.neighbors, dfs(nei)];
        }

        return clone;
    }

    return dfs(node);
};

// 재귀를 활용한 dfs를 사용한 풀이
// 시간복잡도 O(v + e) -> v(노드의 수) + e(간선의 수) 만큼 탐색을 수행
// 공간복잡도 O(n) -> map이 총 노드의 수 만큼 크기를 가짐

// ------------------------------------

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {
    if (!node) {
        return null;
    }

    const clone = new Node(node.val);

    const clonedNodeMap = new Map().set(clone.val, clone);

    // 이 queue에는 클론이 아니라 원본 노드가 들어가야함(neighbors에 대한 참조 때문)
    const queue = [node];

    while (queue.length > 0) {
        const currentNode = queue.pop();

        const currentNodeClone = clonedNodeMap.get(currentNode.val);

        for (const nei of currentNode.neighbors) {
            if (!clonedNodeMap.has(nei.val)) {
                clonedNodeMap.set(nei.val, new Node(nei.val));
                queue.push(nei);
            }
            
            currentNodeClone.neighbors = [...currentNodeClone.neighbors, clonedNodeMap.get(nei.val)];
        }
    }

    return clone;
};

// 큐를 활용한 bfs를 사용한 풀이
// 시간복잡도 O(v + e) -> v(노드의 수) + e(간선의 수) 만큼 탐색을 수행
// 공간복잡도 O(n) -> map이 총 노드의 수 만큼 크기를 가짐
