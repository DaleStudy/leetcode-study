class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        int visited = 0;
        vector<vector<int>> outdegree(numCourses, vector<int>());
        vector<int> indegree(numCourses, 0);

        for(auto edge : prerequisites) {
            outdegree[edge[0]].push_back(edge[1]);
            indegree[edge[1]]++;
        }

        queue<int> que;
        for(int i = 0; i < numCourses; i++) {
            if(indegree[i] == 0) {
                que.push(i);
                visited++;
            }
        }


        while(!que.empty()) {
            int now = que.front();
            que.pop();

            for(auto next : outdegree[now]) {
                indegree[next]--;
                if(indegree[next] == 0) {
                    visited++;
                    que.push(next);
                }
            }
        }

        return (visited == numCourses ? true : false);
    }
};

