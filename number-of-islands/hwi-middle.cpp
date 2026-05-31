class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // BFS 기반 풀이
        int r = grid.size();
        int c = grid[0].size();
        
        int cnt = 0;
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                if (grid[i][j] == '0')
                {
                    continue;
                }

                cnt++;
                queue<pair<int, int>> q;
                q.push({i, j});
                grid[i][j] = '0'; // 방문 여부를 저장하기 위해 grid를 직접 수정
        
                while (!q.empty())
                {
                    int x, y;
                    tie(x, y) = q.front();
                    q.pop();
    
                    int dx[] = { 0, 1, 0, -1 };
                    int dy[] = { 1, 0, -1, 0 };

                    for (int dir = 0; dir < 4; ++dir)
                    {
                        int nx = x + dx[dir];
                        int ny = y + dy[dir];

                        if (nx < 0 || nx >= r || ny < 0 || ny >= c) continue;
                        if (grid[nx][ny] == '0') continue;

                        grid[nx][ny] = '0';
                        q.push({nx, ny});
                    }
                }
            }
        }

        return cnt;
    }
};
