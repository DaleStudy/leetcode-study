/*
 * time:
 * - add: O(N)
 * - search: O(N)
 *  - N is the length of the word.
 * space: O(M)
 * - M is the number of nodes.
 */
public class WordDictionary {

    private Node root;

    public WordDictionary() {
        root = new Node();
    }

    public void addWord(String word) {
        Node node = root;
        for (char ch : word.toCharArray()) {
            if (!node.subNodes.containsKey(ch)) {
                node.subNodes.put(ch, new Node());
            }
            node = node.subNodes.get(ch);
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word) {
        return helper(root, word);
    }

    public boolean helper(Node node, String word) {
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            if (!node.subNodes.containsKey(ch)) {
                if (ch == '.') {
                    for (char x : node.subNodes.keySet()) {
                        Node child = node.subNodes.get(x);
                        if (helper(child, word.substring(i + 1))) {
                            return true;
                        }
                    }
                }
                return false;
            } else {
                node = node.subNodes.get(ch);
            }
        }
        return node.isEndOfWord;
    }

    private class Node {

        Map<Character, Node> subNodes = new HashMap<>();
        boolean isEndOfWord;
    }

}
