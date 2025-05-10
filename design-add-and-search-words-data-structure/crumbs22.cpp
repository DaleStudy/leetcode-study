#include <iostream>
#include <string>

using namespace std;

struct TrieNode {
	bool isEnd;
	TrieNode* children[26];
	TrieNode() : isEnd(false) {
		for (int i = 0; i < 26; i++)
			children[i] = nullptr;
	}
};

class WordDictionary {
private:
	TrieNode* root;
	bool dfs(string& word, int idx, TrieNode* node) {
		if (!node)
			return (false);
		if (idx == word.size()) // 단어가 끝났을 때만 true
			return (node->isEnd);
		
		char c = word[idx];
		if (c == '.') {
			for (int i = 0; i < 26; i++) {
				if (dfs(word, idx + 1, node->children[i]))
					return (true);
			}
			return (false);
		}
		else {
			return dfs(word, idx + 1, node->children[c - 'a']);
		}
	}

public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
		TrieNode* cur = root;
		for (char c : word) {
			int index = c - 'a';
			if (!cur->children[index])
				cur->children[index] = new TrieNode();
			cur = cur->children[index];
		}
		cur->isEnd = true;
    }
    
    bool search(string word) {
        return dfs(word, 0, root);
    }
};
