#include <vector>
using namespace std;

class Solution {
    public:
        /**
         * @param n: the number of vertices
         * @param edges: the edges of undirected graph
         * @return: the number of connected components
         */
        int countComponents(int n, vector<vector<int>> &edges) {
            vector<vector<int>> adjs(n);
            vector<bool>    visited(n, false);
            int result = 0;
    
            for (auto& edge : edges) {
                adjs[edge[0]].push_back(edge[1]);
                adjs[edge[1]].push_back(edge[0]);
            }
    
            for (int i = 0; i < n; i++) {
                if (!visited[i]) {
                    dfs(i, adjs, visited);
                    result++;
                }
            }
            return result;
        }
    
        void    dfs(int curr, vector<vector<int>>& adjs, vector<bool>& visited) {
            if (visited[curr])
                return ;
            visited[curr] = true;
            for (auto& adj : adjs[curr])
                dfs(adj, adjs, visited);
        }
    };
