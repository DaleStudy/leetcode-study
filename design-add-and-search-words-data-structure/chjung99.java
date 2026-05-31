class WordDictionary {
    Node rootNode;
    public WordDictionary() {
        this.rootNode = new Node();
    }

    public void addWord(String word) {
        Node node = rootNode;

        for (int i = 0; i < word.length(); i++) {
            node = node.childNode.computeIfAbsent(word.charAt(i), key -> new Node());
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word) {
        return dfs(rootNode, word, 0);
    }

    public boolean dfs(Node node, String word, int depth) {
        if (depth == word.length()) return node.isEndOfWord;
        if (word.charAt(depth) == '.') {
            for (Node nextNode: node.childNode.values()) {
                if (dfs(nextNode, word, depth + 1)) return true;
            }
            return false;
        } else {
            Node nextNode = node.childNode.getOrDefault(word.charAt(depth), null);
            if (nextNode == null) return false;
            return dfs(nextNode, word, depth+1);
        }
    }

    static class Node {
        Map<Character, Node> childNode;
        boolean isEndOfWord;

        public Node() {
            this.childNode = new HashMap<>();
            this.isEndOfWord = false;
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

