class WordDictionary {

    private class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isEndOfWord = false;
    }

    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    /**
     *  시간 복잡도: O(n), n = 단어의 길이
     *  공간 복잡도: O(n)
     */
    public void addWord(String word) {
        TrieNode node = root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndOfWord = true;
    }

    /**
     *  시간 복잡도: O(26^n), n = 단어의 길이
     *  공간 복잡도: O(n)
     */
    public boolean search(String word) {
        return searchInNode(word, 0, root);
    }

    private boolean searchInNode(String word, int index, TrieNode node) {
        if (index == word.length()) {
            return node.isEndOfWord;
        }

        char c = word.charAt(index);
        if (c != '.') {
            if (node.children.containsKey(c)) {
                return searchInNode(word, index + 1, node.children.get(c));
            } else {
                return false;
            }
        } else {
            for (TrieNode childNode : node.children.values()) {
                if (searchInNode(word, index + 1, childNode)) {
                    return true;
                }
            }
            return false;
        }
    }
}
