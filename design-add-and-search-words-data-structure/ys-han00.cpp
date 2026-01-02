struct TrieNode {
    unordered_map<char, TrieNode*> child;
    bool isEnd;
    TrieNode() : isEnd(false) {}
};

class WordDictionary {
public:
    TrieNode* root;
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* cur = root;
        for(char c : word) {
            if(cur->child.find(c) == cur->child.end())
                cur->child[c] = new TrieNode();
            cur = cur->child[c];
        }
        cur->isEnd = true;
    }
    
    bool search(string word) {
        bool find = false;
        stack<pair<int, TrieNode*>> sta;

        sta.push({0, root});
        while(!sta.empty()) {
            int now = sta.top().first;
            TrieNode* cur = sta.top().second;
            sta.pop();

            if(now == word.size() && cur->isEnd)
                return true;
            
            if(word[now] == '.') {
                for(auto mp : cur->child)
                    sta.push({now + 1, mp.second});
            } else {
                if(cur->child.find(word[now]) != cur->child.end())
                    sta.push({now + 1, cur->child[word[now]]});
            }
        }
        
        return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */

