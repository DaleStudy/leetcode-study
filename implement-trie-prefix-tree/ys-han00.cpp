struct TrieNode {
    unordered_map<char, TrieNode*> child;
    bool isEnd;
    TrieNode() : isEnd(false) {}
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* cur = root;
        for(char c : word) {
            if(cur->child.find(c) == cur->child.end())
                cur->child[c] = new TrieNode();
            cur = cur->child[c];
        }
        cur->isEnd = true;
    }
    
    bool search(string word) {
        TrieNode* cur = root;
        int now = 0;
        while(now < word.size()) {
            if(cur->child.find(word[now]) == cur->child.end())
                return false;
            cur = cur->child[word[now++]];
        }
        return cur->isEnd;
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = root;
        int now = 0;
        while(now < prefix.size()) {
            if(cur->child.find(prefix[now]) == cur->child.end())
                return false;
            cur = cur->child[prefix[now++]];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

