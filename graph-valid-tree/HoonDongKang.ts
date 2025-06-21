/**
 * [Problem]: [178] Graph Valid Tree
 * (https://www.lintcode.com/problem/178/)
 */

export class Solution {
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    //시간복잡도 O(n+e)
    //공간복잡도 O(n+e)
    validTree(n: number, edges: number[][]): boolean {
        const graph: number[][] = Array.from({ length: n }, () => []);
        for (const [a, b] of edges) {
            graph[a].push(b);
            graph[b].push(a);
        }

        const visited = new Set<number>();

        function hasCycle(node: number, prev: number): boolean {
            if (visited.has(node)) return true;
            visited.add(node);

            for (const neighbor of graph[node]) {
                if (neighbor === prev) continue;
                if (hasCycle(neighbor, node)) return true;
            }
            return false;
        }

        if (hasCycle(0, -1)) return false;

        return visited.size === n;
    }

    //시간복잡도 O(n)
    //공간복잡도 O(n)
    validTree2(n: number, edges: number[][]): boolean {
        if (edges.length !== n - 1) return false;

        const graph: number[][] = Array.from({ length: n }, () => []);
        for (const [a, b] of edges) {
            graph[a].push(b);
            graph[b].push(a);
        }

        const visited = new Set<number>();

        function dfs(node: number) {
            visited.add(node);
            for (const neighbor of graph[node]) {
                if (!visited.has(neighbor)) {
                    dfs(neighbor);
                }
            }
        }

        dfs(0);

        return visited.size === n;
    }
}
