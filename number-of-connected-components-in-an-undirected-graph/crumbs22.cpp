/*

*/
class Solution {
public:
    int countComponents(int n, vector<vector<int>> &edges) {
        vector<vector<int>> graph(n);
        vector<bool> visited(n, false);

        for (auto edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, graph, visited);
                cnt++;
            }
        }
        return cnt;
    }

    void dfs(int node, vector<vector<int>> &graph, vector<bool> &visited) {
        visited[node] = true;
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, graph, visited);
            }
        }
    }
};
