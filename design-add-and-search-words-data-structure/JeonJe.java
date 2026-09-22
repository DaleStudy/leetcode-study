import java.util.*;

// L = 단어/패턴 길이, N = 저장된 단어 수, d = 패턴 속 '.' 개수(문제 제약상 최대 2)
// TC: addWord O(L), search O(26^d * L)
// SC: O(N * L)
class WordDictionary {

    public static final int ALPHABET_SIZE = 26;
    public static final char DOT = '.';

    static class TrieNode {
        boolean isWord;
        TrieNode[] children = new TrieNode[ALPHABET_SIZE];

        public TrieNode getChild(char c) {
            return children[c - 'a'];
        }

        public void setChild(char c, TrieNode node) {
            children[c - 'a'] = node;
        }

    }

    TrieNode root;


    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode cur = root;

        for (char c : word.toCharArray()) {
            TrieNode node = cur.getChild(c);
            if (node == null) {
                node = new TrieNode();
                cur.setChild(c, node);
            }
            cur = node;
        }
        cur.isWord = true;
    }


    public boolean search(String word) {
        return dfs(root, word, 0);
    }

    private boolean dfs(TrieNode node, String word, int idx) {
        if (node == null) {
            return false;
        }

        if (idx == word.length()) {
            return node.isWord;
        }

        char c = word.charAt(idx);
        if (c != DOT) {
            return dfs(node.getChild(c), word, idx + 1);
        }

        // '.'은 자식 전부로 갈래가 갈라지고, 하나라도 성공하면 매칭
        for (TrieNode child : node.children) {
            if (dfs(child, word, idx + 1)) {
                return true;
            }
        }

        return false;
    }
}
