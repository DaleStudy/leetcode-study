import java.util.HashMap;
import java.util.Map;

// 한 글자씩 잘라서 하위 자식 노드들로 관리
// search 동작은 기존 그대로 Map자료구조에서 찾고, 이후 prefix연산에서 속도를 개선 (230ms -> 30ms)
class Trie {

    private Trie[] child;
    private Character val;
    private Map<String, Boolean> cMap;

    public Trie() {
        this.cMap = new HashMap<>();
        this.val = null;
    }
    
    public void insert(String word) {
        if(this.cMap.containsKey(word)) return;

        this.cMap.put(word, true);
        this.innerInsert(word);
    }

    public void innerInsert(String word) {
        if(word.length() == 0) return;

        if(this.child == null) {
            this.child = new Trie[26];
        }
        
        char c = word.charAt(0);
        int idx = c - 97;
    
        if(this.child[idx] == null) {
            this.child[idx] = new Trie();
            this.child[idx].val = c;
        }

        this.child[idx].innerInsert(word.substring(1));
    }
    
    public boolean search(String word) {
        return this.cMap.containsKey(word);
    }

    // public boolean search(String word) {
       
    // }
    
    public boolean startsWith(String word) {
        if(word.length() == 0) {
            return true;
        }

        char c = word.charAt(0);
        int idx = c - 97;
        if(this.child == null || this.child[idx] == null || this.child[idx].val == null) return false;


        return this.child[idx].startsWith(word.substring(1));
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */


 // Map으로 풀려버려서 당황..
// 이진트리? 어떤식으로 풀어야 할지 자료구조 정하고 다시 풀어보기..
class BeforeTrie {

    Map<String, Boolean> tMap;

    public BeforeTrie() {
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

