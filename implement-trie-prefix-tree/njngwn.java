// Time Complexity: O(n), n: word.length()
// Space Complexity: O(n), n: word.length()
class Trie {
    private static class TrieNode {
        HashMap<Character, TrieNode> trieNodeMap;
        boolean isEnd;

        private TrieNode() {
            this.trieNodeMap = new HashMap<>();
            this.isEnd = false;
        }
    }

    private TrieNode rootNode;

    public Trie() {
        this.rootNode = new TrieNode();
    }

    public void insert(String word) {
        TrieNode currentNode = this.rootNode;

        for (char ch : word.toCharArray()) {
            if (!currentNode.trieNodeMap.containsKey(ch)) {
                currentNode.trieNodeMap.put(ch, new TrieNode());
            }
            currentNode = currentNode.trieNodeMap.get(ch);
        }
        currentNode.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode currentNode = this.rootNode;

        for (char ch : word.toCharArray()) {
            if (!currentNode.trieNodeMap.containsKey(ch)) {
                return false;
            }
            currentNode = currentNode.trieNodeMap.get(ch);
        }

        return currentNode.isEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode currentNode = this.rootNode;

        for (char ch : prefix.toCharArray()) {
            if (!currentNode.trieNodeMap.containsKey(ch)) {
                return false;
            }
            currentNode = currentNode.trieNodeMap.get(ch);
        }

        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
