/**
	연결 리스트를 통해, 트리 구조를 만들고 탐색하는 방식
*/
class Trie {
    public Map<Character, WordNode> wordMap;

    public Trie() {
        wordMap = new HashMap<>();
    }
    
    public void insert(String word) {
        WordNode wordNode = null;
        char ch = word.charAt(0);
        wordNode = wordMap.get(ch);

        if(wordNode == null) {
            boolean isFirstWord = word.length() == 1;
            wordNode = new WordNode(ch, isFirstWord);
            wordMap.put(ch, wordNode);
        }

        for(int idx = 1; idx < word.length(); idx++) {
            char target = word.charAt(idx);
            boolean isLeaf = word.length() - 1 == idx;
            wordNode = wordNode.next.computeIfAbsent(target, key -> new WordNode(key, isLeaf));
        }
        wordNode.isLeaf = true;
    }
    
    public boolean search(String word) {
        
        WordNode wordNode = null;
        char ch = word.charAt(0);
        wordNode = wordMap.get(ch);
        if (wordNode == null) return false;
        
        
        for(int idx = 1; idx < word.length(); idx++) {
            char target = word.charAt(idx);
            if (!wordNode.next.containsKey(target)) {
                return false;
            }
            wordNode = wordNode.next.get(target);
        }

        return wordNode.isLeaf;
    }
    
    public boolean startsWith(String word) {
        
        WordNode wordNode = null;
        char ch = word.charAt(0);
        wordNode = wordMap.get(ch);
        if (wordNode == null) return false;
        
        
        for(int idx = 1; idx < word.length(); idx++) {
            char target = word.charAt(idx);
            if (!wordNode.next.containsKey(target)) {
                return false;
            }
            wordNode = wordNode.next.get(target);
        }

        return true;
    }
}

class WordNode {
    char ch;
    Map<Character, WordNode> next;
    boolean isLeaf;

    public WordNode(char ch) {
        this(ch, false);
    }
    
    public WordNode(char ch, boolean isLeaf) {
        next = new HashMap<>();
        this.ch = ch;
        this.isLeaf = isLeaf;
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
