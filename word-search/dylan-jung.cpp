class Solution {
public:
    vector<vector<char>> g_board;
    int m, n;
    int dx[4] = { -1, 1, 0, 0 };
    int dy[4] = { 0, 0, -1, 1 };
    bool visited[6][6];

    bool hasWord(string word, int idx, int r, int c) {
        if(idx >= word.size()) return true;
        if(!(0 <= r && r < n && 0 <= c && c < m)) return false;
        if(g_board[r][c] != word[idx]) return false;
        if(visited[r][c]) return false;
        visited[r][c] = true;
        // cout << r << " " << c << " " << word[idx] << "\n";
        for(int i = 0; i < 4; i++) {
            int nr = r + dx[i];
            int nc = c + dy[i];
            if(hasWord(word, idx+1, nr, nc))
                return true;
        }
        visited[r][c] = false;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        g_board = board;
        n = board.size();
        m = board[0].size();
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(g_board[i][j] == word[0]) {
                    fill(&visited[0][0], &visited[0][0]+36, false);
                    if(hasWord(word, 0, i, j)) return true;
                }
            }
        }
        return false;
    }
};
