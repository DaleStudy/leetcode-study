import java.util.ArrayList;
import java.util.List;

class Solution {

    private int[] dx = {0, 0, 1, -1};
    private int[] dy = {1, -1, 0, 0};

    private int m;
    private int n;

    class TrieNode {
        // 단어는 영어 소문자만으로 이루어짐
        TrieNode[] nodes = new TrieNode[26];
        String word = null;
    }

    private void insert(TrieNode root, String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.nodes[idx] == null) {
                node.nodes[idx] = new TrieNode();
            }
            node = node.nodes[idx];
        }
        // 단어
        node.word = word;
    }

    public List<String> findWords(char[][] board, String[] words) {

        List<String> existingWords = new ArrayList<>();

        // 탐색 최적화를 위해 TrieNode 생성
        TrieNode root = new TrieNode();
        for (String word : words) {
            insert(root, word);
        }

        m = board.length;
        n = board[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(board, i, j, root, existingWords);
            }
        }

        return existingWords;
    }

    private void dfs(char[][] board, int i, int j, TrieNode node, List<String> existingWords) {

        char c = board[i][j];

        // 방문 처리 되었거나 TrieNode에 없는 글자라면 탐색 X => Pruning
        if (c == '#' || node.nodes[c - 'a'] == null) {
            return;
        }

        node = node.nodes[c - 'a'];

        // node의 완성된 단어가 있다면
        if (node.word != null) {
            existingWords.add(node.word);
            node.word = null;
        }

        // 방문 처리
        board[i][j] = '#';

        for (int idx = 0; idx < 4; idx++) {
            int ni = i + dx[idx];
            int nj = j + dy[idx];
            if (isRange(ni, nj)) {
                dfs(board, ni, nj, node, existingWords);
            }
        }

        board[i][j] = c;
    }

    // 탐색 범위 조건
    private boolean isRange(int i, int j) {
        return i >= 0 && j >= 0 && i < m && j < n;
    }

}

