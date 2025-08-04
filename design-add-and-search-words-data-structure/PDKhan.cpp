class Trie{
    public:
        Trie* children[26];
        bool isEnd;
    
        Trie(){
            for(int i = 0; i < 26; i++)
                children[i] = nullptr;
            
            isEnd = false;
        }
    };
    
    class WordDictionary {
    private:
        Trie* trie;
    public:
        WordDictionary() {
            trie = new Trie();
        }
        
        void addWord(string word) {
            Trie* node = trie;
    
            for(char ch : word){
                int index = ch - 'a';
    
                if(node->children[index] == nullptr)
                    node->children[index] = new Trie();
                
                node = node->children[index];
            }
    
            node->isEnd = true;
        }
        
        bool dfs(Trie* node, int index, string word){
            if(node == nullptr)
                return false;
    
            if(index == word.length())
                return node->isEnd;
            
            char ch = word[index];
    
            if(ch == '.'){
                for(int i = 0; i < 26; i++){
                    if(dfs(node->children[i], index + 1, word) == true)
                        return true;
                }
            }else
                return dfs(node->children[ch-'a'], index + 1, word);
            
            return false;
        }
    
        bool search(string word) {
            return dfs(trie, 0, word);
        }
    };
