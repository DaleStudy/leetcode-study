/*
    time: O(n+m), where n is the number of nodes and m is the number of edges in the graph.
    space: O(n)
 */
class Solution {

    public int countComponents(int n, int[][] edges) {
        boolean[] visited = new boolean[n];

        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int[] edge : edges) {
            map.computeIfAbsent(edge[0], k -> new ArrayList<>())
               .add(edge[1]);
            map.computeIfAbsent(edge[1], k -> new ArrayList<>())
               .add(edge[0]);
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            dfs(i, map, visited);
            ans++;
        }
        return ans;
    }

    public void dfs(int k, Map<Integer, List<Integer>> map, boolean[] visited) {
        if (visited[k]) {
            return;
        }
        visited[k] = true;
        if (!map.containsKey(k)) {
            return;
        }
        List<Integer> values = map.get(k);
        for (int v : values) {
            dfs(v, map, visited);
        }
    }
}
