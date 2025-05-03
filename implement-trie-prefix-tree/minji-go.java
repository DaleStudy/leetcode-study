/**
 * <a href="https://leetcode.com/problems/implement-trie-prefix-tree/">week05-3.implement-trie-prefix-tree</a>
 * <li>Description: Implement the Trie class    </li>
 * <li>Topics: Hash Table, String, Design, Trie </li>
 * <li>Time Complexity: O(N*K), Runtime 40ms    </li>
 * <li>Space Complexity: O(N*K), Memory 56.07MB  </li>
 */
class Trie {
    private boolean end;
    private final Map<Character, Trie> children;

    public Trie() {
        children = new HashMap<>();
    }

    public void insert(String word) {
        Trie node = this;
        for(Character c : word.toCharArray()) {
            node = node.children.computeIfAbsent(c, k -> new Trie());
        }
        node.end = true;
    }

    public boolean search(String word) {
        Trie node = this;
        for(Character c : word.toCharArray()) {
            node = node.children.get(c);
            if(node == null) {
                return false;
            }
        }
        return node.end;
    }

    public boolean startsWith(String prefix) {
        Trie node = this;
        for(Character c : prefix.toCharArray()) {
            node = node.children.get(c);
            if(node == null) {
                return false;
            }
        }
        return node != null;
    }
