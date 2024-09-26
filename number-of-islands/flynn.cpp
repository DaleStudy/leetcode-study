/**
 * 풀이
 * - bfs를 활용합니다
 * 
 * Big O
 * - M: grid의 행의 수
 * - N: grid의 열의 수
 * 
 * - Time complexity: O(MN)
 *   - 각 좌표는 최대 한 번씩만 조회하게 됩니다
 * - Space complexity: O(MN)
 *   - 방문 여부를 기록하기 위해 visit 배열이 사용됩니다
 *   - queue에 쌓이는 원소의 개수는 최대 MN개까지 증가할 수 있습니다
 */

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        vector<vector<bool>> visit;
        for (int r = 0; r < m; ++r) {
            vector<bool> row;
            for (int c = 0; c < n; ++c) {
                row.push_back(false);
            }
            visit.push_back(row);
        }

        pair<int, int> dirs[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        int res = 0;
        queue<pair<int, int>> q;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (visit[r][c] == false && grid[r][c] == '1') {
                    ++res;
                    q.push({r, c});
                    while (!q.empty()) {
                        auto p = q.front();
                        q.pop();
                        for (auto dir : dirs) {
                            pair<int, int> next = {p.first + dir.first, p.second + dir.second};
                            if (0 <= next.first && next.first < m && 0 <= next.second && next.second < n) {
                                if (visit[next.first][next.second] == false && grid[next.first][next.second] == '1') {
                                    q.push(next);
                                    visit[next.first][next.second] = true;
                                }
                            }
                        }
                    }
                }
            }
        }

        return res;
    }
};
