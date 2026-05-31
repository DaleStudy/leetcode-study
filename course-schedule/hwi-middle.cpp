class Solution {
private:
    enum class eVisitStatus 
    {
        Unvisited, 
        Visiting,
        Visited 
    };

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);

        for (auto& p : prerequisites) 
        {
            int course = p[0];
            int prerequisite = p[1];

            graph[course].push_back(prerequisite);
        }

        vector<eVisitStatus> status(numCourses, eVisitStatus::Unvisited);

        for (int i = 0; i < numCourses; ++i) 
        {
            if (status[i] == eVisitStatus::Unvisited) 
            {
                if (!dfs(i, graph, status)) 
                {
                    return false;
                }
            }
        }

        return true;
    }

private:
    bool dfs(int course, vector<vector<int>>& graph, vector<eVisitStatus>& status) 
    {
        if (status[course] == eVisitStatus::Visiting) 
        {
            return false;
        }

        if (status[course] == eVisitStatus::Visited) 
        {
            return true;
        }

        status[course] = eVisitStatus::Visiting;

        for (int prerequisite : graph[course]) 
        {
            if (!dfs(prerequisite, graph, status)) 
            {
                return false;
            }
        }

        status[course] = eVisitStatus::Visited;
        return true;
    }
};
