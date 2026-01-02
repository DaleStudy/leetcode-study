// class Solution {
// public:
//     vector<int> spiralOrder(vector<vector<int>>& matrix) {
//         int n = matrix.size(), m = matrix[0].size();
//         vector<int> sorted;
//         vector<vector<bool>> check(n, vector<bool>(m, false));
//         queue<pair<int, pair<int, int>>> que;

//         int dx[4] = {-1, 0, 1, 0};
//         int dy[4] = {0, 1, 0, -1};
//         // 0: up, 1: right, 2: down, 3: left
//         que.push({1, {0, 0}});
//         sorted.push_back(matrix[0][0]);
//         check[0][0] = true;
//         while(!que.empty()) {
//             int d = que.front().first;
//             int x = que.front().second.first;
//             int y = que.front().second.second;
//             que.pop();
            
//             int new_x = x + dx[d];
//             int new_y = y + dy[d];
//             if(new_x >= 0 && new_y >= 0 && new_x < n && new_y < m && check[new_x][new_y] == false) {
//                 check[new_x][new_y] = true;
//                 sorted.push_back(matrix[new_x][new_y]);
//                 que.push({d, {new_x, new_y}});
//                 continue;
//             }
//             d = (d + 1) % 4;
//             new_x = x + dx[d];
//             new_y = y + dy[d];
//             if(new_x >= 0 && new_y >= 0 && new_x < n && new_y < m && check[new_x][new_y] == false) {
//                 check[new_x][new_y] = true;
//                 sorted.push_back(matrix[new_x][new_y]);
//                 que.push({d, {new_x, new_y}});
//             }
//         }

//         return sorted;
//     }
// };

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        int top = 0, down = n - 1, left = 0, right = m - 1;
        vector<int> sorted;
        while(top <= down && left <= right) {
            for(int i = left; i <= right; i++)
                sorted.push_back(matrix[top][i]);
            top++;
            
            for(int i = top; i <= down; i++)
                sorted.push_back(matrix[i][right]);
            right--;

            if(top <= down) {
                for(int i = right; i >= left; i--)
                    sorted.push_back(matrix[down][i]);
                down--;
            }
            
            if(left <= right) {
                for(int i = down; i >= top; i--)
                    sorted.push_back(matrix[i][left]);
                left++;
            }
        }

        return sorted;
    }
};

