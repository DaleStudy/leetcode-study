/*
# Time Complexity: O(n)
# Space Complexity: O(n + m)
  - m은 edges.length

# Solution
edges[0][0]에서 출발하여 인접한 모든 edge를 DFS로 순회한다.
  - cycle이 있는 경우 (이미 방문한 적이 있는 node를 재방문)
  - 순회를 마쳤는데 방문하지 않은 node가 있는 경우
위 2경우는 invalid tree이고, 그렇지 않으면 valid tree이다.
*/
class Solution {
    public ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
    public boolean[] visited;
    public boolean validTree(int n, int[][] edges) {
        if (edges.length == 0) {
            return n == 1;
        }

        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            adj.get(a).add(b);
            adj.get(b).add(a);
        }

        if (!dfs(-1, edges[0][0])) {
            return false;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                return false;
            }
        }

        return true;
    }

    public boolean dfs(int prev, int curr) {
        visited[curr] = true;

        for (Integer next : adj.get(curr)) {
            if (next == prev) {
                continue;
            }

            if (visited[next]) {
                return false;
            }

            if (!dfs(curr, next)) {
                return false;
            }
        }

        return true;
    }
}
