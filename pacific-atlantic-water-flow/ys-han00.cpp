// class Solution {
// public:
//     vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
//         int m = heights.size(), n = heights[0].size();
//         int dx[] = {-1, 0, 1, 0};
//         int dy[] = {0, 1, 0, -1};

//         vector<vector<int>> ans;

//         for(int i = 0; i < m; i++) {
//             for(int j = 0; j < n; j++) {
//                 bool pacific = false, atlantic = false;
//                 queue<pair<int, pair<int, int>>> que;
//                 vector<vector<bool>> check(m, vector<bool> (n, false));

//                 que.push({heights[i][j], {i, j}});
//                 check[i][j] = true;        
//                 while(!que.empty()) {
//                     int h = que.front().first;
//                     int x = que.front().second.first;
//                     int y = que.front().second.second;
//                     que.pop();

//                     for(int k = 0; k < 4; k++) {
//                         int new_x = x + dx[k];
//                         int new_y = y + dy[k];

//                         if(new_x == -1 || new_y == -1) 
//                             pacific = true;
//                         if(new_x == m || new_y == n)
//                             atlantic = true;
                        
//                         if(-1 < new_x && new_x < m && -1 < new_y && new_y < n && check[new_x][new_y] == false && heights[new_x][new_y] <= h) {
//                             que.push({heights[new_x][new_y], {new_x, new_y}});
//                             check[new_x][new_y] = true;
//                         }
//                     }

//                     if(pacific && atlantic)
//                         break;
//                 }
//                 if(pacific && atlantic)
//                     ans.push_back(vector<int> {i, j});
//             }
//         }
//         return ans;
//     }
// };

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, 1, 0, -1};
        int m = heights.size(), n = heights[0].size();
        vector<vector<bool>> atlantic(m, vector<bool> (n, false)), pacific(m, vector<bool> (n, false));
        queue<pair<int, int>> que;

        for(int i = 0; i < m; i++) {
            que.push({i, 0});
            pacific[i][0] = true;
        }

        for(int i = 1; i < n; i++) {
            que.push({0, i});
            pacific[0][i] = true;
        }

        while(!que.empty()) {
            int x = que.front().first;
            int y = que.front().second;
            que.pop();

            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx < 0 || nx == m || ny < 0 || ny == n)
                    continue;

                if(heights[x][y] <= heights[nx][ny] && !pacific[nx][ny]) {
                    pacific[nx][ny] = true;
                    que.push({nx, ny});
                }
            }
        }

        for(int i = 0; i < m; i++) {
            que.push({i, n - 1});
            atlantic[i][n - 1] = true;
        }

        for(int i = 0; i < n - 1; i++) {
            que.push({m - 1, i});
            atlantic[m - 1][i] = true;
        }

        while(!que.empty()) {
            int x = que.front().first;
            int y = que.front().second;
            que.pop();

            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx < 0 || nx == m || ny < 0 || ny == n)
                    continue;

                if(heights[x][y] <= heights[nx][ny] && !atlantic[nx][ny]) {
                    atlantic[nx][ny] = true;
                    que.push({nx, ny});
                }
            }
        }

        vector<vector<int>> ans;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(pacific[i][j] && atlantic[i][j])
                    ans.push_back({i, j});
        return ans;
    }
};

