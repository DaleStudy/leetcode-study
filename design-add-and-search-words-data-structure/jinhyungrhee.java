class TrieNode {
    boolean word;
    TrieNode[] children;

    TrieNode() {
        this.word = false;
        this.children = new TrieNode[27];
    }
}

class WordDictionary {
    /**
     * space-complexity : O(N * L) (w.c)
     *  - N : 단어 수, L : 평균 길이
     *  - 단어 하나 추가 시 최대 L개의 TrieNode 생성
     *  - (w.c) 모든 단어가 중복 없이 추가되면 (N*L)개의 노드 필요
     */
    TrieNode root;
    public WordDictionary() {
        this.root = new TrieNode();
    }

    /**
     * addWord() Time-complexity : O(L)
     *  - 각 문자마다 TrieNode를 따라 내려가며 필요한 경우 새 노드 생성
     *  - 한 단어당 최대 L개의 노드 생성 및 접근
     */
    public void addWord(String word) {

        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                curr.children[c - 'a'] = new TrieNode();
            }
            curr = curr.children[c - 'a'];
        }
        curr.word = true;
    }

    /**
     * search() Time-complexity :
     *  - '.'가 없는 경우 : O(L)
     *      -> 일반적인 문자는 한 경로만 탐색
     *  - '.'가 있는 경우 : O(26^L) (w.c)
     *      -> 현재 노드의 모든 자식에 대해 DFS 수행
     *
     */
    public boolean search(String word) {
        return dfs(word, 0, root);
    }

    public boolean dfs(String word, int index, TrieNode node) {

        if (index == word.length()) {
            return node.word;
        }

        char c = word.charAt(index);

        if (c == '.') {
            for (TrieNode child : node.children) {
                if (child != null && dfs(word, index + 1, child)) {
                    return true;
                }
            }
            return false;

        } else {

            TrieNode next = node.children[c - 'a'];
            return next != null && dfs(word, index + 1, next);

        }
    }
}
