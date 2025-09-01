/*
m : word length
n : Trie node count
addWord
Time Complexity: O(m)

search
Time Complexity: O(n)

Space Complexity: O(26 × N × M)

Trie + Dfs
*/

class WordDictionary {
    class TrieNode {
        TrieNode[] children;
        boolean isEnd;

        public TrieNode() {
            children = new TrieNode[26];
            isEnd = false;
        }
    }

    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode current = root;

        for (char str : word.toCharArray()) {
            int idx = str - 'a';
            if (current.children[idx] == null) {
                current.children[idx] = new TrieNode();
            }
            current = current.children[idx];
        }
        current.isEnd = true;
    }
    
    public boolean search(String word) {
        return dfsSearch(word, 0, root);
    }

    private boolean dfsSearch(String word, int idx, TrieNode node) {
        if (idx == word.length()) {
            return node.isEnd;
        }

        char c = word.charAt(idx);
        if (c == '.') {
            for (int i = 0 ; i < 26; i++) {
                if (node.children[i] != null) {
                    if (dfsSearch(word, idx + 1, node.children[i])) {
                        return true;
                    }
                }
            }
            return false;
        } else {
            int charIdx = c - 'a';
            if (node.children[charIdx] == null) {
                return false;
            }
            return dfsSearch(word, idx + 1, node.children[charIdx]);
        }
    }
}
