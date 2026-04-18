import java.util.HashMap;
import java.util.Map;

class WordDictionary {


    Map<Character, WordDictionary> map;
    boolean isEnd = false;

    public WordDictionary() {
        map = new HashMap<>();
    }
    
    public void addWord(String word) {
        char ch = word.charAt(0);
        WordDictionary node;
        if (map.containsKey(ch)) {
            node = map.get(ch);
        } else {
            node = new WordDictionary();
        }

        map.put(ch, node);

        if (word.length() == 1) {
            node.isEnd = true;
            return;    
        }

        node.addWord(word.substring(1));
    }
    
    public boolean search(String word) {
        if (word.length() == 0) {
            return isEnd;
        }

        char ch = word.charAt(0);
        WordDictionary node;

        if (ch == '.') {
            for (Map.Entry<Character, WordDictionary> entry : map.entrySet()) {
                if (entry.getValue().search(word.substring(1))){
                    return true;
                }
            }
        }

        if (map.containsKey(ch)) {
            node = map.get(ch);
            return node.search(word.substring(1));
        }

        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
