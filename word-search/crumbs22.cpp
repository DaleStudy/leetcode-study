#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
		// 단어 시작점을 탐색, 시작점 찾으면 dfs 시작하고 마지막 단어까지 도달 가능할 때 true 반환
        for (int i = 0; i < board.size(); i++) {
			for (int j = 0;  j < board[0].size(); j++) {
				if (board[i][j] == word[0] && dfs(board, i, j, 0, word)) {
					return (true);
				}
			}
		}
		return (false);
    }
	bool dfs(vector<vector<char>>& board, int i, int j, int idx, string& word)  {
		if (idx == word.size())
			return (true);
		if (i < 0 || i >= board.size() || \
			j < 0 || j >= board[0].size() || \
			board[i][j] != word[idx]) {
				return (false);
		}

		char tmp = board[i][j];

		// 방문 표시
		board[i][j] = '1';

		// 4방향으로 탐색
		bool found = dfs(board, i + 1, j, idx + 1, word) || dfs(board, i - 1, j, idx + 1, word) || \
					dfs(board, i, j + 1, idx + 1, word) || dfs(board, i, j - 1, idx + 1, word);
		
		// 다른 경로 탐색을 위해서 방문 표시를 원래대로 복원
		board[i][j] = tmp;
		return (found);
	}
};
