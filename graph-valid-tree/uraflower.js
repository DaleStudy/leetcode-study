/**
 * @param {number} n
 * @param {number[][]} edges
 * @returns {boolean}
 */
function validTree(n, edges) {
    //  트리의 조건을 만족하는지 확인(V = E + 1)
    if (edges.length !== n - 1) {
        return false;
    }

    const graph = Array.from({ length: n }).map(() => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const queue = [[-1, 0]]; // 부모 노드, 자식 노드
    const visited = new Set();

    while (queue.length) {
        const [parent, current] = queue.shift();
        if (visited.has(current)) {
            return false;
        }
        visited.add(current);

        for (const neighbor of graph[current]) {
            if (neighbor === parent) continue;
            queue.push([current, neighbor]);
        }
    }

    return visited.size === n;
}

// 시간복잡도: O(V + E)
// 공간복잡도: O(V)
