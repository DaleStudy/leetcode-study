class Solution {
public:
    int m, n;
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};

    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (dfs(board, word, i, j, 0))
                    return true; 

        return false;
    }

    bool dfs(vector<vector<char>>& board, string& word, int x, int y, int idx) {
        if (idx == word.size()) return true;

        if (x < 0 || y < 0 || x >= m || y >= n || board[x][y] != word[idx])
            return false;

        char temp = board[x][y];
        board[x][y] = '*'; 

        bool found = false;
        for (int k = 0; k < 4; k++)
            if (dfs(board, word, x + dx[k], y + dy[k], idx + 1)) {
                found = true;
                break;
            }

        board[x][y] = temp;

        return found;
    }
};

