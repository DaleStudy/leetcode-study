/*
Time Complexity (n = length of word/prefix)
- initialization: O(1)
- insert: O(n)
- search: O(n)
- startsWith: O(n)

Space Complexity: O(n * c) (c = calls)
- 길이 3인 알파벳 소문자 문자열의 가짓수 : 26^3 = 17,576
- 길이 4인 알파벳 소문자 문자열의 가짓수 : 26^4 = 456,976
만약 n이 3 이하였다면, 3만 번의 call 동안 trie가 포화되어 공간 복잡도가 O(26 * n) = O(n) 이었을 것.
하지만 n이 2,000으로 충분히 크기 때문에 trie가 포화되지는 않을 것이므로, 공간 복잡도는 O(n * c).
*/
class Trie {

    class Node {
        public char val;
        public boolean ends;
        public HashMap<Character, Node> children;

        Node() {
            this.children = new HashMap<>();
        }
    }

    public Node root;

    public Trie() {
        this.root = new Node();
    }

    public void insert(String word) {
        Node curr = this.root;

        for (char ch : word.toCharArray()) {
            curr = curr.children.computeIfAbsent(ch, c -> new Node());
            curr.val = ch;
        }
        curr.ends = true;
    }

    public boolean search(String word) {
        Node curr = this.root;

        for (char ch : word.toCharArray()) {
            curr = curr.children.get(ch);
            if (curr == null)
                return false;
        }
        return curr.ends;
    }

    public boolean startsWith(String prefix) {
        Node curr = this.root;

        for (char ch : prefix.toCharArray()) {
            curr = curr.children.get(ch);
            if (curr == null)
                return false;
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
