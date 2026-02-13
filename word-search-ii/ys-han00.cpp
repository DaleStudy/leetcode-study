struct TrieNode {
    TrieNode* children[26];
    string* word; 

    TrieNode() {
        for (int i = 0; i < 26; i++) children[i] = nullptr;
        word = nullptr;
    }
};

class Solution {
    int rows, cols;
    vector<string> output;

    void insert(TrieNode* root, const string& word) {
        TrieNode* curr = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!curr->children[idx]) curr->children[idx] = new TrieNode();
            curr = curr->children[idx];
        }
        curr->word = const_cast<string*>(&word); 
    }

    void dfs(vector<vector<char>>& board, int r, int c, TrieNode* node) {
        char ch = board[r][c];
        int idx = ch - 'a';

        if (idx < 0 || !node->children[idx]) return;

        TrieNode* nextNode = node->children[idx];
        
        if (nextNode->word != nullptr) {
            output.push_back(*(nextNode->word));
            nextNode->word = nullptr; 
        }

        board[r][c] = '#'; 

        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] != '#') {
                dfs(board, nr, nc, nextNode);
            }
        }

        board[r][c] = ch;
    }

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (const string& w : words) insert(root, w);

        rows = board.size();
        cols = board[0].size();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                dfs(board, r, c, root);
            }
        }

        return output;
    }
};

