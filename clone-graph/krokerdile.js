/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {
    if (!node) return null;

    const visited = new Map(); // 원본 노드 -> 복제 노드

    function dfs(curr) {
        if (visited.has(curr)) {
            return visited.get(curr); // 이미 복제한 경우
        }

        const copy = new _Node(curr.val);
        visited.set(curr, copy); // 복제한 노드 저장

        for (const neighbor of curr.neighbors) {
            copy.neighbors.push(dfs(neighbor)); // 이웃도 재귀적으로 복사
        }

        return copy;
    }

    return dfs(node);
};

