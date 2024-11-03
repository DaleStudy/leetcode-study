// V는 정점, E는 간선
// 시간 복잡도: O(V + E)
// 공간 복잡도: O(V + E)

class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n, edges) {
        const visited = Array.from({length: n}, () => false);
        const graph = new Map();

        for (const [v, d] of edges) {
            if (!graph.has(v)) graph.set(v, []);
            if (!graph.has(d)) graph.set(d, []);

            graph.get(v).push(d);
            graph.get(d).push(v);
        }

        const dfs = (node) => {
            visited[node] = true
            for (let nei of graph.get(node) || []) {
                if (!visited[nei]) dfs(nei)
            }
        }

        let count = 0;
        for (let i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i);
                count++;
            }
        }


        return count
    }
}
