/*
 * time: O(M)
 * space: O(N*M)
 */
public class TrieNode {
    private static final int MAX_SIZE = 26;

    public TrieNode[] subNodes;
    public boolean isEndOfWord;

    public TrieNode() {
        subNodes = new TrieNode[MAX_SIZE];
    }

    public boolean contains(char ch) {
        return subNodes[ch - 'a'] != null;
    }

    public TrieNode getSubNode(char ch) {
        return subNodes[ch - 'a'];
    }

    public void put(char ch, TrieNode node) {
        subNodes[ch - 'a'] = node;
    }

    @Override
    public String toString() {
        return "TrieNode{sub=" + Arrays.toString(subNodes) + "}";
    }
}


class Trie {

    public TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            if (!node.contains(ch)) {
                node.put(ch, new TrieNode());
            }
            node = node.getSubNode(ch);
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            if (node == null) {
                return false;
            }
            if (!node.contains(word.charAt(i))) {
                return false;
            }
            node = node.getSubNode(word.charAt(i));
            if (i == word.length() - 1 && node.isEndOfWord) {
                return true;
            }
        }
        return false;
    }

    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (int i = 0; i < prefix.length(); i++) {
            if (node == null) {
                return false;
            }
            if (!node.contains(prefix.charAt(i))) {
                return false;
            }
            node = node.getSubNode(prefix.charAt(i));
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
