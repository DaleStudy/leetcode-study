// GPT의 풀이. 트리를 이용해 O(m)으로 해결했다.
public class Trie {
    private class TrieNode {
        TrieNode[] children;
        boolean isEndOfWord;

        public TrieNode() {
            children = new TrieNode[26];  // 알파벳 a~z (26개의 자식 노드)
            isEndOfWord = false;          // 해당 노드가 단어의 끝인지 아닌지 나타냄
        }
    }

    private TrieNode root;

    public Trie() {
        root = new TrieNode();  // 루트 노드 초기화
    }

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';  // 알파벳을 0-25의 숫자로 변환
            if (node.children[index] == null) {
                node.children[index] = new TrieNode();  // 해당 문자가 없으면 새 노드를 생성
            }
            node = node.children[index];  // 자식 노드로 이동
        }
        node.isEndOfWord = true;  // 단어의 끝을 표시
    }

    public boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                return false;  // 해당 문자가 없으면 false 반환
            }
            node = node.children[index];  // 자식 노드로 이동
        }
        return node.isEndOfWord;  // 단어의 끝인지를 확인
    }

    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                return false;  // 해당 접두사로 시작하는 단어가 없으면 false 반환
            }
            node = node.children[index];  // 자식 노드로 이동
        }
        return true;  // 접두사로 시작하는 단어가 있으면 true 반환
    }
}

// 백트래킹으로 풀어봤는데, 속도가 너무 안나왔음
// O(n*m)의 시간복잡도가 나옴. n은 글자수 m은 글자길이
class Trie {

    private List<String> words;

    public Trie() {
        words = new ArrayList<>();
    }

    public void insert(String word) {
        words.add(word);
    }

    public boolean search(String word) {
        return backtrack(word, true);
    }

    public boolean startsWith(String prefix) {
        return backtrack(prefix, false);
    }

    private boolean backtrack(String target, boolean exactMatch) {
        for (String word : words) {
            if (exactMatch) {
                if (word.equals(target)) {
                    return true;
                }
            } else {
                if (word.startsWith(target)) {
                    return true;
                }
            }
        }
        return false;
    }
}
