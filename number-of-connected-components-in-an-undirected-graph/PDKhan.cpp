class Solution {
    public:
        /**
         * @param n: the number of vertices
         * @param edges: the edges of undirected graph
         * @return: the number of connected components
         */
        void dfs(int curr, vector<vector<int>>& graph, vector<bool>& visited){
            visited[curr] = true;
    
            for(int i = 0; i < graph[curr].size(); i++){
                if(visited[graph[curr][i]] == false)
                    dfs(graph[curr][i], graph, visited);
            }
        }
    
        int countComponents(int n, vector<vector<int>> &edges) {
            // write your code here
            vector<bool> visited(n, 0);
            vector<vector<int>> graph (n);
            int cnt = 0;
    
            for(int i = 0; i < edges.size(); i++){
                graph[edges[i][0]].push_back(edges[i][1]);
                graph[edges[i][1]].push_back(edges[i][0]);
            }
    
            for(int i = 0; i < n; i++){
                if(visited[i] == false){
                    dfs(i, graph, visited);
                    cnt++;
                }
            }
            
            return cnt;
        }
    };
