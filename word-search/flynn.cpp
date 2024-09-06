/**
 * 풀이
 * - dfs와 backtracking을 이용하여 풀었습니다
 * 
 * Big-O
 * - M: 주어진 grid `board`의 행 수
 * - N: 주어진 grid `board`의 열 수
 * - W: 주어진 string `word`의 size
 * 
 * - Time complexity: O(M * N * 3 ^ W)
 *   - `exist`함수가 grid 원소 모두를 조회합니다 -> O(M * N)
 *   - 만약 `dfs`함수가 실행될 경우, 해당 함수는 최대 3방향에 대해 재귀호출을 실행합니다 (이전 좌표로는 `dfs`를 호출하지 않기 때문)
 *   - 재귀 호출 스택의 크기는 주어진 string `word`의 길이에 비례합니다 -> O(3^W)
 *   
 * - Space complexity: O(M * N + W)
 *   - 재귀 호출 스택의 크기는 주어진 string `word`의 길이에 비례합니다 -> O(W)
 *   - 탐색 여부를 기록하는 `visit` 배열의 크기는 `board`와 같습니다 -> O(M * N)
 */

class Solution {
public:
    bool dfs(vector<vector<char>>& board, string word, vector<vector<bool>>& visit, int idx, int r, int c) {
        if (word.size() - 1 == idx) return true;

        pair<int, int> dirs[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int R = board.size();
        int C = board[0].size();

        visit[r][c] = true;

        int next_idx = idx + 1;
        
        bool res = false;

        for (auto dir : dirs) {
            int next_r = r + dir.first;
            int next_c = c + dir.second;

            if (0 <= next_r && next_r < R && 0 <= next_c && next_c < C && !visit[next_r][next_c]) {
                if (board[next_r][next_c] == word[next_idx] && dfs(board, word, visit, next_idx, next_r, next_c)) {
                    res = true;
                    break;
                }
            }
        }

        visit[r][c] = false;

        return res;
    }

    bool exist(vector<vector<char>>& board, string word) {
        int R = board.size();
        int C = board[0].size();
        vector<vector<bool>> visit;
        for (int i = 0; i < R; i++) {
            vector<bool> tmp;
            for (int j = 0; j < C; j++) {
                tmp.push_back(false);
            }
            visit.push_back(tmp);
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i][j] == word[0] && dfs(board, word, visit, 0, i, j)) return true;
            }
        }

        return false;
    }
};
