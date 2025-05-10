import java.util.HashMap;
import java.util.Map;

/**
 *  WordDictionary
 * WordDictionary() - 객체 초기화
 * void addWord(word) - 자료 구조에 word 추가
 * boolean search(word) - 자료 구조에 word 있으면 true 아니면 false 반환
 - '.'는 와일드카드로 활용 가능
 */
class WordDictionary {

    private Node root;

    public WordDictionary() {
        root = new Node();
    }

    public void addWord(String word) {
        Node current = root;
        for (char c : word.toCharArray()) {
            if (!current.nodeCharacters.containsKey(c)) {
                current.nodeCharacters.put(c, new Node());
            }
            current = current.nodeCharacters.get(c);
        }
        current.isEnd = true;
    }

    public boolean search(String word) {
        return searchInNode(word, 0, root);
    }

    private boolean searchInNode(String word, int idx, Node node) {

        if (node == null) {
            return false;
        }

        if (idx == word.length()) {
            return node.isEnd;
        }

        char c = word.charAt(idx);
        // 와일드카드는 Node에 있는 전체 값 다 탐색
        if (c == '.') {
            for (Node child : node.nodeCharacters.values()) {
                if (searchInNode(word, idx + 1, child)) {
                    return true;
                }
            }
            return false;
        } else {
            Node current = node.nodeCharacters.get(c);
            return searchInNode(word, idx + 1, current);
        }
    }

    static class Node {

        boolean isEnd;

        Map<Character, Node> nodeCharacters;

        Node() {
            nodeCharacters = new HashMap<>();
            isEnd = false;
        }

    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

