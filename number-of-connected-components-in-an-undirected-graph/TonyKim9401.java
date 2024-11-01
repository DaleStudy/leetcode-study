// TC: O(n + m)
// n = the number of nodes, m = the number of edges
// SC: O(n + m)
// n, m are the each size of the 2 demension array 'edges'
public class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());

        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        boolean[] visit = new boolean[n];
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (!visit[i]) {
                count += 1;
                dfs(i, graph, visit);
            }
        }
        return count;
    }

    private void dfs(int node, List<List<Integer>> graph, boolean[] visit) {
        visit[node] = true;
        for (int neighbor : graph.get(node)) {
            if (!visit[neighbor]) dfs(neighbor, graph, visit);
        }
    }
}
