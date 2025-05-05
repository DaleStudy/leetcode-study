/**
 * <a href="https://leetcode.com/problems/design-add-and-search-words-data-structure/">week06-3.design-add-and-search-words-data-structure</a>
 * <li>Description: Design a data structure that supports adding new words and finding if a string matches any previously added string</li>
 * <li>Topics: String, Depth-First Search, Design, Trie </li>
 * <li>Time Complexity: O(N), Runtime 274ms             </li>
 * <li>Space Complexity: O(N), Memory 118.44MB          </li>
 */
class WordDictionary {
    private Trie dictionary;

    public WordDictionary() {
        dictionary = new Trie();
    }

    public void addWord(String word) {
        dictionary.add(word);
    }

    public boolean search(String word) {
        return dictionary.contains(word);
    }

}

public class Trie {
    private boolean isEnd;
    private Map<Character, Trie> next;

    Trie() {
        next = new HashMap<>();
    }

    public void add(String word) {
        Trie trie = this;
        for(char c : word.toCharArray()){
            trie = trie.next.computeIfAbsent(c, k -> new Trie());
        }
        trie.isEnd = true;
    }

    public boolean contains(String word) {
        Trie trie = this;
        for(int i=0; i<word.length(); i++){
            char c = word.charAt(i);
            if(c == '.') {
                for(Trie newTrie : trie.next.values()) {
                    if(newTrie.contains(word.substring(i+1))){
                        return true;
                    }
                }
                return false;
            } else {
                trie = trie.next.get(c);
                if(trie == null) {
                    return false;
                }
            }
        }

        return trie.isEnd;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
