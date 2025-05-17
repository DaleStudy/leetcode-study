class WordDictionary {
    private static class TrieNode {
        boolean isEnd;
        Map<Character, TrieNode> children;

        TrieNode() {
            this.isEnd = false;
            this.children = new HashMap<>();
        }
    }

    private final TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            node.children.putIfAbsent(ch, new TrieNode());
            node = node.children.get(ch);
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(root, word, 0);
    }

    private boolean dfs(TrieNode node, String word, int index) {
        if (index == word.length()) {
            return node.isEnd;
        }

        char ch = word.charAt(index);
        if (ch == '.') {
            for (TrieNode child : node.children.values()) {
                if (dfs(child, word, index + 1)) {
                    return true;
                }
            }
            return false;
        }

        TrieNode next = node.children.get(ch);
        if (next == null) {
            return false;
        }

        return dfs(next, word, index + 1);
    }
}

