import java.util.ArrayList;
import java.util.List;

/**
 * brute-force로 먼저 접근한 423ms의 최악의 성능 코드.
 */
class Trie {

    private List<String> list;

    public Trie() {
        this.list = new ArrayList<>();
    }

    public void insert(String word) {
        this.list.add(word);
    }

    public boolean search(String word) {
        for(String s : list) {
            if(s.equals(word)) return true;
        }
        return false;
    }

    public boolean startsWith(String prefix) {
        for(String s : list) {
            if(s.startsWith(prefix)) return true;
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