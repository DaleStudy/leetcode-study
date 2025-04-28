/*
    풀이:
        dfs를 이용해 board의 각 칸에서 출발해서 4방향으로 board를 탐색
        word[index]와 일치하는 글자의 칸이 있으면 index + 1 시키면서 단어 끝 index까지 탐색

        - 탐색 중인 칸을 다른 char(#)로 바꿔서 이미 경로상에 있는 칸이라고 표시해주고 탐색 끝난 후 다시 되돌린다
        - board를 변경할 수 없다면 unordered_set(해시테이블)로 중복 방문을 제거하거나 bool[row][col] 이중 배열로 방문된 칸 표시

    board 크기 : M * N, word 길이 W

    TC : O(M * N * 4^W)
        board 전체 순회하고 각 칸 마다 4방향으로 word길이 만큼 재귀호출

    SC : O(W)
        재귀호출 스택이 word의 길이와 비례
*/

class Solution {
    public:
        bool exist(vector<vector<char>>& board, string word) {
            for (int i = 0; i < board.size(); ++i) {
                for (int j = 0; j < board[0].size(); ++j) {
                    if (dfs(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
            return false;
        }
    private:
        bool dfs(vector<vector<char>>& board, const string& word, int i, int j, int index) {
            if (index == word.size())
                return true;
            if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size())
                return false;
            if (board[i][j] != word[index])
                return false;
    
            char tmp = board[i][j];
    
            board[i][j] = '#';
            bool found = dfs(board, word, i + 1, j, index + 1) ||
                        dfs(board, word, i - 1, j, index + 1) ||
                        dfs(board, word, i, j + 1, index + 1) ||
                        dfs(board, word, i, j - 1, index + 1);
            board[i][j] = tmp;
    
            return found;
        }
    };
