class Solution {
private:
    int row;
    int col;

public:
    bool exist(vector<vector<char>>& board, string word) {
        row = board.size();
        col = board[0].size();
        for (int r = 0; r < row; ++r)
        {
            for (int c = 0; c < col; ++c)
            {
                if (solve(board, word, r, c, 0))
                {
                    return true;
                }
            }
        }

        return false;
    }

    // dfs 함수
    bool solve(vector<vector<char>>& board, string& word, int r, int c, int idx)
    {
        // 범위를 벗어난 경우
        if (r < 0 || r >= row || c < 0 || c >= col) 
        {
            return false;
        }

        // 글자가 맞지 않는 경우
        if (board[r][c] != word[idx])
        {
            return false;
        }

        // 단어를 찾은 경우
        if (idx == word.size() - 1)
        {
            return true;
        }
        
        char ch = board[r][c];
        board[r][c] = '?'; // 이미 방문한 곳으로 돌아오지 않도록 입력으로 들어오지 않는 문자로 치환

        // 상하좌우 탐색
        int dr[4] = { 1, 0, -1, 0 };
        int dc[4] = { 0, 1, 0, -1 };

        for (int dir = 0; dir < 4; ++dir)
        {
            int nr = r + dr[dir];
            int nc = c + dc[dir];
            if (solve(board, word, nr, nc, idx + 1))
            {
                return true;
            }
        }
        
        board[r][c] = ch; // 원래 문자로 되돌리기
        return false;
    }
};
