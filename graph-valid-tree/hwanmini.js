// V: Node 개수, E: 간선의 개수
// 시간복잡도: O(V + E)
// 공간복잡도: O(V + E)

class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {boolean}
     */
    validTree(n, edges) {
        const graph = new Map();

        for (let [u, v] of edges) {
            if (!graph.has(u)) graph.set(u, [])
            if (!graph.has(v)) graph.set(v, [])
            graph.get(u).push(v)
            graph.get(v).push(u)
        }

        const visited = Array.from({length: n}, () => false);

        let edgeCount = 0;
        const queue = [0];
        visited[0] = true

        while(queue.length) {
            const cur = queue.shift();

            for (const edge of graph.get(cur) || []) {
                if (!visited[edge]) {
                    visited[edge] = true;
                    queue.push(edge)
                }
                edgeCount++;
            }
        }

        const isAllVisited = visited.every((visited) => visited === true)

        return isAllVisited && (edgeCount / 2) === (n - 1)
    }


}
