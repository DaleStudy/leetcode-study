class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int r = heights.size();
        int c = heights[0].size();
        
        vector<vector<int>> result;
        if (r == 0 || c == 0) return result;

        vector<vector<bool>> pacific(r, vector<bool>(c, false));
        vector<vector<bool>> atlantic(r, vector<bool>(c, false));
        
        queue<pair<int, int>> pacific_q;
        queue<pair<int, int>> atlantic_q;

        for (int i = 0; i < r; ++i) 
        {
            pacific_q.push({i, 0});
            pacific[i][0] = true;
            
            atlantic_q.push({i, c - 1});
            atlantic[i][c - 1] = true;
        }

        for (int j = 0; j < c; ++j) 
        {
            pacific_q.push({0, j});
            pacific[0][j] = true;
            
            atlantic_q.push({r - 1, j});
            atlantic[r - 1][j] = true;
        }

        bfs(pacific_q, pacific, heights);
        bfs(atlantic_q, atlantic, heights);

        for (int i = 0; i < r; ++i) 
        {
            for (int j = 0; j < c; ++j) 
            {
                if (pacific[i][j] && atlantic[i][j]) 
                {
                    result.push_back({i, j});
                }
            }
        }

        return result;
    }

private:
    void bfs(queue<pair<int, int>>& q, vector<vector<bool>>& visited, const vector<vector<int>>& heights) 
    {
        int r = heights.size();
        int c = heights[0].size();
        
        int dx[] = { 0, 1, 0, -1 };
        int dy[] = { 1, 0, -1, 0 };

        while (!q.empty()) {
            int x, y;
            tie(x, y) = q.front();
            q.pop();

            for (int dir = 0; dir < 4; ++dir) 
            {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx < 0 || nx >= r || ny < 0 || ny >= c) continue;
                
                if (visited[nx][ny]) continue;
                
                if (heights[nx][ny] < heights[x][y]) continue;

                visited[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
};
