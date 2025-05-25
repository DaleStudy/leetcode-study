// Definition for a _Node.
function _Node(val, neighbors) {
    this.val = val === undefined ? 0 : val;
    this.neighbors = neighbors === undefined ? [] : neighbors;
};

/**
 * 그래프를 깊은 복사하여 반환하는 함수
 * @param {_Node} node
 * @return {_Node}
 */
const cloneGraph = function (node) {
    if (!node) return null;

    function dfs(node, visited) {
        const current = new _Node(node.val);
        visited.set(node, current);

        node.neighbors.forEach((neighbor) => {
            const clonedNeighbor = visited.has(neighbor) ? visited.get(neighbor) : dfs(neighbor, visited);
            current.neighbors.push(clonedNeighbor);
        });

        return current;
    }

    return dfs(node, new Map()); // visited: 원본 노드를 key, 클론한 노드를 value로 하는 맵
};

// 시간복잡도: O(V + E) (모든 노드와 간선을 한 번씩 순회)
// 공간복잡도: O(V) (visited 맵 + 재귀 호출 스택)
