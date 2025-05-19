import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


// NOTE: dot에 대한 wildcard 검색이 핵심이었던 문제.
// NOTE: tc -> 문자 입력 O(n), 패턴검색 O(26^n), 패턴X검색 O(1)

/** 
  검색어    | 의미
    "."    |  길이가 1인 아무 문자와 매치
    ".a"   |  길이 2: 첫 글자는 아무 문자, 두 번째는 a
    "..d"  |  길이 3: 처음 두 글자는 아무 문자, 마지막은 d
    "..."  |  길이 3인 모든 단어와 매치
*/ 
class WordDictionary {

    private WordDictionary[] child;
    private Character val;
    private Map<String, Boolean> cMap;

    public WordDictionary() {
         this.cMap = new HashMap<>();
        this.val = null;
    }
    
    public void addWord(String word) {
        if(this.cMap.containsKey(word)) return;

        this.cMap.put(word, true);
        this.innerInsert(word);
    }

    public void innerInsert(String word) {
        if(word.length() == 0) return;

        if(this.child == null) {
            this.child = new WordDictionary[26];
        }
        
        char c = word.charAt(0);
        int idx = c - 97;
    
        if(this.child[idx] == null) {
            this.child[idx] = new WordDictionary();
            this.child[idx].val = c;
        }

        this.child[idx].innerInsert(word.substring(1));
    }
    
    public boolean search(String word) {
        if(!word.contains(".")) return this.cMap.containsKey(word);


        return this.patternSearch(word);
    }

    private boolean patternSearch(String wildcard) {
        if(wildcard.length() == 0) return true;

        char c = wildcard.charAt(0);
        if(c == '.') { // NOTE: wildcard를 만났을 때, 해당 depth는 검사하지 않고, 다음 번(자식) 문자들에 대해서 검색 이어나가기.
            List<Boolean> res = new ArrayList<>();

            for(WordDictionary children : this.child) {
                if(children != null) {
                    res.add(children.patternSearch(wildcard.substring(1)));
                }
            }

            for(boolean b : res) {
                if(b) return true;
            }

            return false;
        } 
        
        int idx = c - 97;
        if(this.child == null || this.child[idx] == null || this.child[idx].val == null) return false;

        return this.child[idx].patternSearch(wildcard.substring(1));
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */


// 이전 TRIE 자료구조를 모른 채로 풀이했던 문제..
class PrevWordDictionary {

    private String word;
    private PrevWordDictionary leftChild;
    private PrevWordDictionary rightChild;

    public PrevWordDictionary() {
        this.leftChild = null;
        this.rightChild = null;
        this.word = null;
    }
    
    public void addWord(String word) {
        if(this.word == null) {
            this.word = word;
            return;
        }

        // NOTE: 사전 순으로 크고 작음을 두어 이진처리.
        if(this.word.compareTo(word) == 1) {

            this.rightChild = new PrevWordDictionary();
            this.rightChild.addWord(word);
        } else if (this.word.compareTo(word) == -1) {

            this.leftChild = new PrevWordDictionary();
            this.leftChild.addWord(word);
        } else {
            // already exists. just return
        }
    }
    
    public boolean search(String word) {
        if(word.contains(".")) {
            //  String replaced = word.replace(".", "");

            // return word.startsWith(".") ? this.startsWith(replaced) : this.endsWith(replaced);           
            return this.patternSearch(word.replace(".", ""));
        }

        if(this.word == null) {
            return false;
        }

        if(this.word.equals(word)) {
            return true;
        }

        if(this.rightChild == null && this.leftChild == null) {
            return false;
        }

        if(this.word.compareTo(word) == 1) {
            return this.rightChild == null ? false : this.rightChild.search(word);
        } else {
            return this.leftChild == null ? false : this.leftChild.search(word);
        }
    }

    private boolean patternSearch(String wildcard) {
        if(this.word.contains(wildcard)) return true;
        
        boolean left = false;
        boolean right = false;
        if(this.leftChild != null) {
           left = this.leftChild.patternSearch(wildcard);
        }

        if(this.rightChild != null) {
           right = this.rightChild.patternSearch(wildcard);
        }

        return left || right;
    }
}
