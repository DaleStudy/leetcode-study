class WordDictionary {

    private static class Node {
        Node[] next = new Node[26];
        boolean isEnd;
    }

    private final Node root = new Node();

    public WordDictionary() {}

    public void addWord(String word) {
        Node cur = root;
        for (int k = 0; k < word.length(); k++) {
            char ch = word.charAt(k);
            int i = ch - 'a';
            if (cur.next[i] == null) cur.next[i] = new Node();
            cur = cur.next[i];
        }
        cur.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(word, 0, root);
    }

    private boolean dfs(String word, int idx, Node node) {
        if (node == null) return false;
        if (idx == word.length()) return node.isEnd;

        char ch = word.charAt(idx);
        if (ch == '.') {
            // 모든 가능 문자로 한 글자 매칭
            for (int c = 0; c < 26; c++) {
                if (node.next[c] != null && dfs(word, idx + 1, node.next[c])) {
                    return true;
                }
            }
            return false;
        } else {
            return dfs(word, idx + 1, node.next[ch - 'a']);
        }
    }
}
