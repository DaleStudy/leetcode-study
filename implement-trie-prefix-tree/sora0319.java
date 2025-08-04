class Trie {
    Set<String> dict;

    public Trie() {
        dict = new TreeSet<>();
    }

    public void insert(String word) {
        dict.add(word);
    }

    public boolean search(String word) {
        if(dict.contains(word)) return true;
        return false;
    }

    public boolean startsWith(String prefix) {
        for(String saved : dict){
            int count = 0;
            if(prefix.compareTo(saved) > 0) continue;
            if(prefix.length() > saved.length()) continue;

            for(int i = 0; i < prefix.length(); i++){
                if(prefix.charAt(i) != saved.charAt(i)) break;
                count++;
            }
            if(count == prefix.length()) return true;
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

