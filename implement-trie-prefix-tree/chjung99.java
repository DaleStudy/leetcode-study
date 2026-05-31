class Trie {
    Node rootNode = new Node();

    public Trie() {

    }

    public void insert(String word) {
        Node node = this.rootNode;

        for (int i = 0; i < word.length(); i++) {
            node = node.childNode.computeIfAbsent(word.charAt(i), key -> new Node());
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word) {
        Node node = this.rootNode;

        for (int i = 0; i < word.length(); i++) {
            node = node.childNode.getOrDefault(word.charAt(i), null);
            if (node == null) return false;
        }
        return node.isEndOfWord;
    }

    public boolean startsWith(String prefix) {
        Node node = this.rootNode;

        for (int i = 0; i < prefix.length(); i++) {
            node = node.childNode.getOrDefault(prefix.charAt(i), null);
            if (node == null) return false;
        }
        return true;
    }

    static class Node {
        Map<Character, Node> childNode = new HashMap<>();
        boolean isEndOfWord = false;

        public Node(){

        }
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */




