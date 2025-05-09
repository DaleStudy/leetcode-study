class TrieNode {
    boolean word;
    TrieNode[] children;

    TrieNode() {
        this.word = false;
        this.children = new TrieNode[27];
    }
}

class WordDictionary {
    TrieNode root;
    public WordDictionary() {
        this.root = new TrieNode();
    }

    public void addWord(String word) {

        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                curr.children[c - 'a'] = new TrieNode();
            }
            curr = curr.children[c - 'a'];
        }
        curr.word = true;
    }

    public boolean search(String word) {
        return dfs(word, 0, root);
    }

    public boolean dfs(String word, int index, TrieNode node) {

        if (index == word.length()) {
            return node.word;
        }

        char c = word.charAt(index);

        if (c == '.') {
            for (TrieNode child : node.children) {
                if (child != null && dfs(word, index + 1, child)) {
                    return true;
                }
            }
            return false;

        } else {

            TrieNode next = node.children[c - 'a'];
            return next != null && dfs(word, index + 1, next);

        }
    }
}
