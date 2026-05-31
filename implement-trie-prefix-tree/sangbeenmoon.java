import java.util.HashMap;
import java.util.Map;

class Trie {

    Map<Character, Trie> map;
    boolean isEnd = false;

    public Trie() {
        map = new HashMap<>();
    }

    public void insert(String word) {
        Trie trie;
        if (map.containsKey(word.charAt(0))) {
            trie = map.get(word.charAt(0));
        } else {
            trie = new Trie();
        }
        map.put(word.charAt(0), trie);

        if (word.length() == 1) {
            map.get(word.charAt(0)).isEnd = true;
            return;
        }

        trie.insert(word.substring(1));
    }

    public boolean search(String word) {
        if (map.containsKey(word.charAt(0))) {
            if (word.length() == 1) {
                return map.get(word.charAt(0)).isEnd;
            }
            return map.get(word.charAt(0)).search(word.substring(1));
        }
        return false;
    }

    public boolean startsWith(String prefix) {
        if (map.containsKey(prefix.charAt(0))) {
            if (prefix.length() == 1) {
                return true;
            }
            return map.get(prefix.charAt(0)).startsWith(prefix.substring(1));
        }
        return false;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
