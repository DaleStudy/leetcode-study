//DFS
class Solution {
    public:
        bool dfs(int curr, vector<vector<int>>& graph, vector<int>& visited){
            if(visited[curr] == 1)
                return false;
            
            if(visited[curr] == 2)
                return true;
    
            visited[curr] = 1;
    
            for(int i = 0; i < graph[curr].size(); i++){
                if(dfs(graph[curr][i], graph, visited) == false)
                    return false;
            }
    
            visited[curr] = 2;
    
            return true;
        }
    
        bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
            vector<vector<int>> graph (numCourses);
            vector<int> visited (numCourses, 0);
    
            for(int i = 0; i < prerequisites.size(); i++){
                int course = prerequisites[i][0];
                int pre = prerequisites[i][1];
    
                graph[pre].push_back(course);
            }
    
            for(int i = 0; i < numCourses; i++){
                if(dfs(i, graph, visited) == false)
                    return false;
            }
    
            return true;
        }
    };

// BFS
class Solution {
    public:
        bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
            vector<vector<int>> graph (numCourses);
            vector<int> inDegree (numCourses, 0);
    
            for(int i = 0; i < prerequisites.size(); i++){
                int course = prerequisites[i][0];
                int pre = prerequisites[i][1];
    
                graph[pre].push_back(course);
                inDegree[course]++;
            }
    
            queue<int> q;
    
            for(int i = 0; i < numCourses; i++){
                if(inDegree[i] == 0)
                    q.push(i);
            }
    
            int count = 0;
    
            while(!q.empty()){
                int curr = q.front();
                q.pop();
                count++;
    
                for(int i = 0; i < graph[curr].size(); i++){
                    if(--inDegree[graph[curr][i]] == 0)
                        q.push(graph[curr][i]);
                }
            }
    
            return count == numCourses;;
        }
    };
