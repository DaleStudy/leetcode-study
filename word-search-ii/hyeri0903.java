class Solution {
    /**
     * 너무 어려워서 풀이 봤어요 ㅠㅠ
     */
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        String word;
    }

    List<String> result = new ArrayList<>();
    int m, n;
    char[][] board;

    public List<String> findWords(char[][] board, String[] words) {
        this.board = board;
        this.m = board.length;
        this.n = board[0].length;

        TrieNode root = buildTrie(words);

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                dfs(i, j, root);
            }
        }
        return result;
    }
    private TrieNode buildTrie(String[] words) {
    TrieNode root = new TrieNode();

    for(String word : words) {
        TrieNode curr = root;

        for(char ch : word.toCharArray()) {
            int idx = ch - 'a';

            if(curr.children[idx] == null) {
                curr.children[idx] = new TrieNode();
            }

            curr = curr.children[idx];
        }

        curr.word = word;
        }

        return root;
    }
    void dfs(int i, int j, TrieNode node) {
        //boundary check
        if(i < 0 || i >= m || j < 0 || j >= n) return;
        //이미 방문했으면 return
        if(board[i][j] == '#') return;

        char ch = board[i][j];
        if(node.children[ch - 'a'] == null) return;

        node = node.children[ch - 'a'];

        if(node.word != null) {
            result.add(node.word);
            node.word = null;   //중복방지 체크
        }
        
        board[i][j] = '#';  //방문 체크

        dfs(i+1, j, node);
        dfs(i-1, j, node);
        dfs(i, j+1, node);
        dfs(i, j-1, node);

        //backtracking
        board[i][j] = ch;
    }
  
}
