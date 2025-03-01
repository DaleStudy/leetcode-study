/*
# Time Complexity: O(n)
# Space Comlexity: O(n + m)
  - m = edges.length
*/
class Solution {
    public int countComponents(int n, int[][] edges) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            adj.get(a).add(b);
            adj.get(b).add(a);
        }

        boolean[] visited = new boolean[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            dfs(i, visited, adj);
            ans++;
        }

        return ans;
    }

    public void dfs(int curr, boolean[] visited, ArrayList<ArrayList<Integer>> adj) {
        visited[curr] = true;

        for (Integer next : adj.get(curr)) {
            if (visited[next]) continue;
            dfs(next, visited, adj);
        }
    }
}
