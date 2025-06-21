/**
 * [Problem]: [3651] Number of Connected Components in an Undirected Graph
 * (https://www.lintcode.com/problem/3651/)
 */
export class Solution {
    /**
     * @param n: the number of vertices
     * @param edges: the edges of undirected graph
     * @return: the number of connected components
     */
    countComponents(n: number, edges: number[][]): number {
        //시간복잡도 O(n + e)
        // 공간복잡도 O(n + e)
        function dfsFunc(n: number, edges: number[][]): number {
            const visited = new Array(n).fill(false);
            const graph: number[][] = Array.from({ length: n }, () => []);

            for (const [node, adjacent] of edges) {
                graph[node].push(adjacent);
                graph[adjacent].push(node);
            }

            function dfs(node: number) {
                visited[node] = true;
                for (const neighbor of graph[node]) {
                    if (!visited[neighbor]) {
                        dfs(neighbor);
                    }
                }
            }

            let count = 0;

            for (let i = 0; i < n; i++) {
                if (!visited[i]) {
                    count++;
                    dfs(i);
                }
            }

            return count;
        }
        // 시간복잡도 O(n + e)
        // 공간복잡도 O(n + e)
        function stackFunc(n: number, edges: number[][]): number {
            const visited = new Array(n).fill(false);
            const graph: number[][] = Array.from({ length: n }, () => []);
            let count = 0;

            for (const [node, adjacent] of edges) {
                graph[node].push(adjacent);
                graph[adjacent].push(node);
            }

            for (let i = 0; i < n; i++) {
                if (visited[i]) continue;
                count++;
                const stack = [i];

                while (stack.length) {
                    const node = stack.pop()!;
                    visited[node] = true;

                    for (let adj of graph[node]) {
                        if (!visited[adj]) stack.push(adj);
                    }
                }
            }

            return count;
        }
    }
}
