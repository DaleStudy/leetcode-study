class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size(), m = grid[0].size();
        int ans = 0;
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, 1, 0, -1};

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(grid[i][j] == '0')
                    continue;
                
                queue<pair<int, int>> que;
                que.push({i, j});
                grid[i][j] = '0';
                while(!que.empty()) {
                    int x = que.front().first;
                    int y = que.front().second;
                    que.pop();
                    
                    for(int k = 0; k < 4; k++) {
                        int new_x = x + dx[k];
                        int new_y = y + dy[k];
                        if(new_x < 0 || new_x >= n || new_y < 0 || new_y >=m || grid[new_x][new_y] == '0')
                            continue;
                        
                        que.push({new_x, new_y});
                        grid[new_x][new_y] = '0';
                    }
                }
                ans++;
            }
        }

        return ans;
    }
};

