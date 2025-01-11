class Trie {
    /**
    1. understanding
    - Trie data structure
    - To process at most 3 * 10^4 calls in proper time, each call must be under O(N), where N is the length of word.
    - insert: insert data into Trie
    - search: find data from inserted Datas
    - startsWith: find
    2. strategy
    - a) use list to save inserted words
        - insert: O(1)
        - search: O(L * N), where L is the length of list, N is the length of each words.
        - startsWith: O(L * N)
        - total call to be 3 * 10^4, i assume each method call count at most 10^4 or linear correlation in 10^4 scale.
        - so, L <= 10^4, N <= 10^4
        - space: O(L * N)
        - it is enough to pass, but there are duplicates in space and also in excution count.
    - b) 
    */

    private List<String> words;
    public Trie() {
        words = new ArrayList<>();
    }
    
    public void insert(String word) {
        words.add(word);
    }
    
    public boolean search(String word) {
        for (String w: words) {
            if (w.equals(word)) return true;
        }
        return false;
    }
    
    public boolean startsWith(String prefix) {
        for (String w: words) {
            if (w.indexOf(prefix) == 0) return true;
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

