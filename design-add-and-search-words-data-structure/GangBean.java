class WordDictionary {
    private Map<Character, WordDictionary> children;
    private boolean isEnd;

    public WordDictionary() {
        this.children = new HashMap<>();
        this.isEnd = false;
    }
    
    public void addWord(String word) {
        char[] arr = word.toCharArray();
        WordDictionary next = this;
        for (int i = 0; i < arr.length; i++) {
            char c = arr[i];
            next.children.putIfAbsent(c, new WordDictionary());
            next = next.children.get(c);
        }
        next.isEnd = true;
    }
    
    public boolean search(String word) {
        // System.out.println(this);
        return search(word, 0);
    }

    private boolean search(String word, int idx) {
        if (idx == word.length()) return this.isEnd;
        char c = word.charAt(idx);
        if (c == '.') {
            return this.children.values().stream().anyMatch(child -> child.search(word, idx+1));
        }
        if (!this.children.containsKey(c)) return false;
        return this.children.get(c).search(word, idx+1);
    }

    public String toString() {
        return String.format("%s -> %s", isEnd, this.children);
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

