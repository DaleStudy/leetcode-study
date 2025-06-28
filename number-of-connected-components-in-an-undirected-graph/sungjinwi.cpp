/*
    풀이 :
        인접리스트 방식으로 그래프를 저장
        visited에 방문한 노드 표시
        노드를 순회하면서 방문하지 않은 노드이면 dfs를 통해 방문으로 표시함 -> 연결된 모든 노드 방문 처리
        component 개수 + 1

        이 로직을 노드 전체에 대해 반복

        정점 개수 : V 간선 개수 : E

        TC : O (V + E)

        SC : O (V + E)

*/

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
