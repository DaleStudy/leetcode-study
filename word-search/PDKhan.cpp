class Solution {
    public:
        bool search(int r, int c, int index, vector<vector<char>>& board, string word){
            if(index == word.length())
                return true;
    
            if(r < 0 || r >= board.size() || c < 0 || c >= board[0].size() || board[r][c] != word[index])
                return false;
            
            char curr = board[r][c];
    
            board[r][c] = '0';
    
            if(search(r + 1, c, index + 1, board, word) == true)
                return true;
            
            if(search(r - 1, c, index + 1, board, word) == true)
                return true;
            
            if(search(r, c + 1, index + 1, board, word) == true)
                return true;
            
            if(search(r, c - 1, index + 1, board, word) == true)
                return true;
            
            board[r][c] = curr;
    
            return false;
        }
    
        bool exist(vector<vector<char>>& board, string word) {
            for(int i = 0; i < board.size(); i++){
                for(int j = 0; j < board[i].size(); j++){
                    if(board[i][j] == word[0]){
                        if(search(i, j, 0, board, word) == true)
                            return true;
                    }
                }
            }
    
            return false;
        }
    };
