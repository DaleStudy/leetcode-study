class TrieNode{
public:
    TrieNode* children[26] = {};
    string word = "";
};

class Solution {
public:
    void insert(TrieNode* root, const string& word){
        TrieNode* node = root;

        for(int i = 0; i < word.length(); i++){
            int idx = word[i] - 'a';

            if(!node->children[idx])
                node->children[idx] = new TrieNode();
            
            node = node->children[idx];
        }
        node->word = word;
    }

    void dfs(int r, int c, vector<vector<char>>& board, TrieNode* root, vector<string>& result){
        if(r < 0 || r >= board.size() || c < 0 || c >= board[r].size())
            return;

        char ch = board[r][c];

        if(ch == '#' || !root->children[ch - 'a'])
            return;
        
        root = root->children[ch - 'a'];

        if(!root->word.empty()){
            result.push_back(root->word);
            root->word.clear();
        }

        board[r][c] = '#';
        
        dfs(r - 1, c, board, root, result);
        dfs(r + 1, c, board, root, result);
        dfs(r, c - 1, board, root, result);
        dfs(r, c + 1, board, root, result);
        
        board[r][c] = ch;
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();

        for(int i = 0; i < words.size(); i++)
            insert(root, words[i]);
        
        vector<string> result;

        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                dfs(i, j, board, root, result);
            }
        }

        return result;
    }
};
