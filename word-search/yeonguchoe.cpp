class Solution {
public:
    bool backtrack(vector<vector<char>>& board, const string& word,
                   int current_row, int current_column, int index) {
        // 이전 iteration까지 backtrack을 통과한 경우
        // index가 단어의 길이와 같아지는 경우
        if (index == word.size()) {
            return true;
        }

        // 탐색중인 cell이 board를 넘어선 경우
        if (current_row < 0 || current_row >= board.size() ||
            current_column < 0 || current_column >= board[0].size()) {
            return false;
        }

        // 탐색중인 cell에 있는 문자가 단어의 문자와 다른 경우
        if (board[current_row][current_column] != word[index]) {
            return false;
        }

        // 탐색중인 cell의 문자를 글자가 아닌것으로 지정하여, 방문 표시
        char temp = board[current_row][current_column];
        board[current_row][current_column] = '#';

        // 탐색중인 cell의 주변을 backtrack으로 탐색
        bool found =
            backtrack(board, word, current_row - 1, current_column,
                      index + 1) or
            backtrack(board, word, current_row, current_column - 1,
                      index + 1) or
            backtrack(board, word, current_row + 1, current_column,
                      index + 1) or
            backtrack(board, word, current_row, current_column + 1, index + 1);

        // 탐색중인 cell의 값을 원래대로 돌려 놓음
        board[current_row][current_column] = temp;

        // 만약에 찾아진 경우, true를 위로 올림
        // 만약에 탐색 도중에 2가지 false를 반환하는 케이스에 걸렸으면 false를
        // 위로 올림
        return found;
    }

    bool exist(vector<vector<char>>& board, string word) {

        // 시작점을 설정
        for (int row = 0; row < board.size(); ++row) {
            for (int col = 0; col < board[0].size(); ++col) {
                // 만약에 backtrack 함수가 true인 경우를 찾았으면, true 반환
                if (backtrack(board, word, row, col, 0)) {
                    return true;
                }
            }
        }
        // true인 경우를 한번도 찾지 못했다면, false 반환
        return false;
    }
};
