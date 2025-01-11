import java.util.HashSet;
import java.util.Set;

// 풀이 1 : 단순 반복문
// 시간 복잡도: N(단어 길이), M(단어 개수) -> O(N*M)
// 공간 복잡도: O(M)
class WordDictionary {

    Set<String> wordSet;
    public WordDictionary() {
        wordSet = new HashSet<>();  
    }
    
    public void addWord(String word) {
       wordSet.add(word);
    }
    
    public boolean search(String word) {
        if(word.contains(".")){
            char[] wordArr = word.toCharArray();
            boolean found = false;
            for(String w: wordSet){
                if(word.length()!=w.length()) continue;
                
                char[] charArr = w.toCharArray();
                for(int i=0;i<charArr.length;i++){
                    if(wordArr[i]=='.') {
                        found=true;
                        continue;
                    }
                    if(wordArr[i]!=charArr[i]) {
                        found=false;
                        break;
                    }
                    found=true;
                }
                if(found) return true;
            }
            return false;
        }
        else{
            return wordSet.contains(word);
        }
    }
}


// 풀이2: trie
// 시간 복잡도: N(단어 길이) -> O(26^N * N)
// 공간 복잡도: O(N * M) - M(단어 개수)
class TrieNode {
    TrieNode[] child;
    boolean isEnd; // flag if the node is end.

    public TrieNode() {
        child = new TrieNode[26]; // 알파벳 개수
        isEnd = false;
    }
}

class WordDictionary {
    TrieNode root;

    public WordDictionary() {
        root = new TrieNode(); // trie 루트 생성
    }

    public void addWord(String word) {
        TrieNode cur = root;
        for (char w : word.toCharArray()) {
            if (cur.child[w - 'a'] == null) {
                cur.child[w - 'a'] = new TrieNode(); // 자식 생성
            }
            cur = cur.child[w - 'a'];
        }
        cur.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(root, word, 0); // dfs 호출 시, index도 전달
    }

    // dfs를 수행하며, 현재 인덱스까지 탐색한 상태에서 단어를 검색
    private boolean dfs(TrieNode cur, String word, int index) {
        // 단어 끝에 도달했으면, 현재 노드가 끝을 나타내는지 확인
        if (index == word.length()) {
            return cur.isEnd;
        }

        char c = word.charAt(index);
        
        // '.' 이면 모든 자식 노드에 대해 재귀적으로 탐색
        if (c == '.') {
            for (TrieNode child : cur.child) {
                if (child != null && dfs(child, word, index + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            // '.'이 아닌 경우, 해당 문자에 해당하는 자식으로 계속 내려감
            if (cur.child[c - 'a'] == null) {
                return false;
            }
            return dfs(cur.child[c - 'a'], word, index + 1);
        }
    }
}

