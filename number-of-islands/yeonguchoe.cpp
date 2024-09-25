class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;

        int row_size = grid.size();
        int column_size = grid[0].size();

        queue<pair<int, int>> q;

        for (int i = 0; i < row_size; i++) {
            for (int j = 0; j < column_size; j++) {
                if (grid[i][j] == '1') {
                    LookAround(i, j, grid, q, row_size, column_size);
                    count += 1;
                }
            }
        }
        return count;
    }

    // BFS
    void LookAround(int& x, int& y, vector<vector<char>>& grid,
                    queue<pair<int, int>>& q, int& row_size, int& column_size) {
        pair<int, int> center_location{x, y};
        q.push(center_location);

        grid[x][y] = '0';

        while (!q.empty()) {
            pair<int, int> selected_location = q.front();
            q.pop();

            int selected_x = selected_location.first;
            int selected_y = selected_location.second;

            // 선택된 cell에서 왼쪽
            if (selected_x - 1 >= 0 &&
                grid[selected_x - 1][selected_y] == '1') {
                q.push({selected_x - 1, selected_y});
                grid[selected_x - 1][selected_y] = '0';
            }

            // 선택된 cell에서 오른쪽
            if (selected_x + 1 < row_size &&
                grid[selected_x + 1][selected_y] == '1') {
                q.push({selected_x + 1, selected_y});
                grid[selected_x + 1][selected_y] = '0';
            }

            // 선택된 cell에서 위쪽
            if (selected_y - 1 >= 0 &&
                grid[selected_x][selected_y - 1] == '1') {
                q.push({selected_x, selected_y - 1});
                grid[selected_x][selected_y - 1] = '0';
            }

            // 선택된 cell에서 아래쪽
            if (selected_y + 1 < column_size &&
                grid[selected_x][selected_y + 1] == '1') {
                q.push({selected_x, selected_y + 1});
                grid[selected_x][selected_y + 1] = '0';
            }
        }
    }
    // 시간 복잡도: O(row*column)
    // 공간 복잡도: O(row*column)
};
