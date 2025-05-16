/*
    풀이 :
        Trie를 활용해서 단어를 저장한다
        글자마다 이어지는 다음 글자에 대한 children[26](알파벳 소문자 개수 26개)를 가지고 현재 글자에서 끝나는지 여부(isEnd)를 가진다

        addWord는 한글자씩 node에 없으면 추가하고 다음 글자의 노드로 이동하며
        word에 대한 반복을 마친 뒤 마지막 node의 isEnd를 1로 바꿈

        search는 한글자씩 다음 노드로 이동하며 word의 끝에 다다랐을 떄 isEnd가 1인지 return
        dfs를 활용하여 '.'이 나올 경우 알파벳 26개 모두에 대해 다음 글자부터 시작하는 dfs를 호출

    word의 길이 : W

    TC : 
        addWord : O(W)
            word 길이에 비례하여 반복문

        search : O(26^W)
            최악의 경우 word길이 만큼 '.'이 있으면 하나하나 마다 26번의 재귀호출이 있다

    SC :
        addWord : O(W)
            TrieNode 개수는 word길이에 비례
        
        search : O(W)
            재귀 호출스택은 word 길이에 비례
*/

class WordDictionary {
    private:
        struct TrieNode {
            int isEnd = 0;
            TrieNode* children[26] = {};
        };
        TrieNode* root;
    
    public:
        WordDictionary() {
            this->root = new TrieNode();
        }
        
        void addWord(string word) {
            TrieNode* node = root;
            for (auto& c : word)
            {
                int idx = c - 'a';
                if (!node->children[idx])
                    node->children[idx] = new TrieNode();
                node = node->children[idx];
            }
            node->isEnd = 1;
        }
        
        bool search(string word) {
            return dfs(word, this->root);
        }
    
        bool dfs(string word, TrieNode* node) {
            if (word.empty())
                return node->isEnd;
    
            for (int i = 0; i < word.size(); i++)
            {
                if (word[i] == '.')
                {
                    for (int j=0; j < 26; j++)
                    {
                        if (node->children[j] && this->dfs(word.substr(i + 1), node->children[j]))
                            return true;
                    }
                    return false;
                }
                int idx = word[i] - 'a';
                if (!node->children[idx])
                    return false;
                node = node->children[idx];
            }
            return node->isEnd;
        }
    };
    
    /**
     * Your WordDictionary object will be instantiated and called as such:
     * WordDictionary* obj = new WordDictionary();
     * obj->addWord(word);
     * bool param_2 = obj->search(word);
     */
