/**
 * 풀이
 * - Trie 구조를 활용하여 풀이할 수 있습니다
 * - wildcard인 '.'에 대한 처리가 필요합니다
 * 
 * Big O
 * - N: 주어지는 문자열 word의 길이
 * - M: 현재 WordDictionary에 저장되어 있는 TrieNode의 수
 * 
 * - void addWord(string word)
 *   - Time complexity: O(N)
 *   - Space complexity: O(N)
 *     - 최악의 경우 word의 모든 문자에 대해 새로운 TrieNode를 추가해야 합니다
 * 
 * - bool search(string word)
 * - bool _search(string word, int idx, TrieNode* node)
 *   - Time complexity: best O(N), worst O(M) < O(26^N)
 *     - wildcard 사용 및 기존에 저장된 word의 상태에 따라 달라집니다
 *   - Space complexity: O(N)
 *     - _search가 재귀적으로 호출되므로 재귀 호출 스택의 깊이만큼 추가적인 공간이 사용됩니다
 *     - 재귀 호출 스택의 깊이는 현재 찾는 word의 길이에 선형적으로 비례합니다
 */

class TrieNode {
public:
    array<TrieNode*, 27> links;
    bool word;

    TrieNode(): word(false) {
        links.fill(nullptr);
    }
};

class WordDictionary {
public:
    WordDictionary(): root(new TrieNode()) {}
    
    void addWord(string word) {
        TrieNode* current = root;
        
        for (char c : word) {
            if (current->links[c - 'a'] == nullptr) {
                current->links[c - 'a'] = new TrieNode();
            }
            current = current->links[c - 'a'];
        }

        current->word = true;
    }
    
    bool search(string word) {
        return _search(word, 0, root);
    }
    
private:
    TrieNode* root;

    bool _search(string word, int idx, TrieNode* node) {
        if (word.size() == idx) return node->word;

        char c = word[idx];

        if (c != '.') {
            if (node->links[c - 'a'] == nullptr) return false;
            
            TrieNode* next_node = node->links[c - 'a'];
            int next_idx = idx + 1;

            return _search(word, next_idx, next_node);
        } else {
            for (TrieNode* link : node->links) {
                if (link != nullptr) {
                    TrieNode* next_node = link;
                    int next_idx = idx + 1;

                    if (_search(word, next_idx, next_node)) return true;
                }
            }
            return false;
        }
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
