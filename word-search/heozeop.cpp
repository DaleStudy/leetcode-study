// time complexity: O(n * m * 3 ^ L), L은 최대 깊이
// spatial complexity: O((n * m ) ^ 2)

class Solution {
public:
  bool exist(vector<vector<char>>& board, string word) {
    vector<vector<bool>> visit;
    for(int i = 0; i < board.size(); ++i) {
      for(int j = 0; j < board[0].size(); ++j) {
        if(board[i][j] != word[0]) continue;
        visit = vector(board.size(), vector(board[0].size(), false));
        visit[i][j] = true;
        if (find(board, word, 1, {i,j}, visit)) {
          return true;
        }
      }
    }

    return false;
  }

  bool find(
    vector<vector<char>>& board, 
    string word, 
    int fi, 
    pair<int,int> curPos, 
    vector<vector<bool>>& visit
  ) {
    if(fi == word.length()) {
      return true;
    }

    char target = word[fi];
    int nr,ny;
    for(int i = 0; i < 4; ++i) {
      nr = curPos.first + DIRECTIONS[i][0];
      ny = curPos.second+ DIRECTIONS[i][1];

      if (isOutSideOfBoard({nr,ny}, {board.size(), board[0].size()}) || visit[nr][ny] || board[nr][ny] != target) {
        continue;
      }

      visit[nr][ny] = true;
      if(find(board, word, fi + 1, {nr,ny}, visit)) {
        return true;
      }
      visit[nr][ny] = false;
    }

    return false;
  }

  int DIRECTIONS[4][2] = {
    {-1, 0},
    {0, 1},
    {1, 0},
    {0, -1},
  };

  bool isOutSideOfBoard(pair<int,int> cur, pair<int,int> boardSize) {
    return cur.first < 0 || cur.second < 0 || cur.first >= boardSize.first || cur.second >= boardSize.second;
  }
};
