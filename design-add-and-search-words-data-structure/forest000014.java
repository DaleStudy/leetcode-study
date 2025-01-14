/*
Time Complexity:
- add: O(w)
- search: O(26^2 * w) = O(w)
Space Complexity: O(w)

Trie를 활용하되, '.'의 탐색이 필요한 경우에는 for문을 사용한다.

*/
class WordDictionary {
    class Node {
        public char ch;
        public boolean ends;
        public Map<Character, Node> children;

        Node() {
            this.children = new HashMap<>();
        }

        Node(char ch) {
            this.ch = ch;
            this.children = new HashMap<>();
        }
    }

    Node root;

    public WordDictionary() {
        this.root = new Node();
    }

    public void addWord(String word) {
        Node curr = this.root;

        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            if (!curr.children.containsKey(ch)) {
                curr.children.put(ch, new Node(ch));
            }

            curr = curr.children.get(ch);
        }

        curr.ends = true;
    }

    public boolean search(String word) {
        return searchChar(word, 0, this.root);
    }

    private boolean searchChar(String word, int idx, Node curr) {
        if (curr == null) {
            return false;
        } else if (idx == word.length()) {
            return curr.ends;
        }

        char ch = word.charAt(idx);

        if (ch == '.') {
            for (Character key : curr.children.keySet()) {
                if (searchChar(word, idx + 1, curr.children.get(key))) {
                    return true;
                }
            }
            return false;
        } else {
            return searchChar(word, idx + 1, curr.children.get(ch));
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
