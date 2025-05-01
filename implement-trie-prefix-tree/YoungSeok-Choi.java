import java.util.HashMap;
import java.util.Map;

// Map으로 풀려버려서 당황..
// 이진트리? 어떤식으로 풀어야 할지 자료구조 정하고 다시 풀어보기..
class Trie {

    Map<String, Boolean> tMap;

    public Trie() {
        this.tMap = new HashMap<>();
    }
    
    public void insert(String word) {
        this.tMap.put(word, true);
    }
    
    public boolean search(String word) {
        return this.tMap.containsKey(word);
    }
    
    public boolean startsWith(String prefix) {
        for(String key : this.tMap.keySet()) {
            if(key.startsWith(prefix)) return true;
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
