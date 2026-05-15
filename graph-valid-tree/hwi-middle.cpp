class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n + 1);
        vector<bool> vis(n + 1);

        for (vector<int>& edge : edges)
        {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        // BFS 수행
        int visited = 1;
        queue<pair<int, int>> q;
        q.push({0, -1});
        while (!q.empty())
        {
            int cur;
            int parent;
            tie(cur, parent) = q.front();
            q.pop();

            for (int n : adj[cur])
            {
                // 자기가 왔던 노드면 넘어감
                if (n == parent)
                {
                    continue;
                }

                // 이미 방문한 노드면 유효하지 않음
                if (vis[n])
                {
                    return false;
                }

                vis[n] = true;
                visited++;
                q.push({n, cur});
            }
        }

        // BFS를 통해 전체 노드를 방문할 수 있었어야 함
        return visited == n;
    }
};
