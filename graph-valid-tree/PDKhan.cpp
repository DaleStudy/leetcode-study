class Solution {
    public:
        bool dfs(int curr, int parent, vector<vector<int>>& graph, vector<int>& visited){
            if(visited[curr])
                return false;
    
            visited[curr] = 1;
    
            for(int i = 0; i < graph[curr].size(); i++){
                if(graph[curr][i] == parent)
                    continue;
    
                if(dfs(graph[curr][i], curr, graph, visited) == false)
                    return false;
            }
    
            return true;
        }
    
        bool validTree(int n, vector<vector<int>> &edges) {
            // write your code here
            if(edges.size() != n - 1)
                return false;
    
            vector<vector<int>> graph (n);
            vector<int> visited (n, 0);
    
            for(int i = 0; i < edges.size(); i++){
                int first = edges[i][0];
                int second = edges[i][1];
    
                graph[first].push_back(second);
                graph[second].push_back(first);
            }
    
            if(dfs(0, -1, graph, visited) == false)
                return false;
            
            for(int i = 0; i < n; i++){
                if(visited[i] == 0)
                    return false;
            }
    
            return true;
        }
    };
