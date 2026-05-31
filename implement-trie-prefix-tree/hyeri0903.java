class Trie {
    class TrieNode {
        TrieNode[] children;
        boolean isEnd;

        public TrieNode() {
            children = new TrieNode[26]; // a ~ z
            isEnd = false;
        }
    }

    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;

        for(char c: word.toCharArray()) {
            int index = c - 'a';
            //처음 들어오는 단어는 node 생성
            if(node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            //다음 노드로 이동
            node = node.children[index];
        }
        //단어의 끝 표시
        node.isEnd = true;
    }
    
    public boolean search(String word) {
        TrieNode node = root;
        for(char c: word.toCharArray()) {
            int index = c - 'a';
            //존재하지 않으면 false return
            if(node.children[index] == null) {
                return false;
            }
            //다음 노드로 이동
            node = node.children[index];
        }
        return node.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        //중간에 null을 안만나면 true 반환
        TrieNode node = root;
        for(char c: prefix.toCharArray()) {
            int index = c - 'a';
            if(node.children[index] == null) {
                return false;
            }
            node = node.children[index];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
